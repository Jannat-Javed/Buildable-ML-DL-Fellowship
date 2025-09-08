import numpy as np
import pandas as pd
from pathlib import Path
from datetime import datetime

class InvalidPathError(Exception):
    pass

class DataGenerationError(Exception):
    pass

class DataGenerator:
    def __init__(self, out_csv, log_file=None, random_state=42):
        self.out_csv = Path(out_csv)
        self.log_file = Path(log_file) if log_file else None
        self.rng = np.random.default_rng(random_state)

    def _log_error(self, msg):
        if self.log_file is not None:
            self.log_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.log_file, 'a', encoding='utf-8') as f:
                f.write(f"[{datetime.now().isoformat()}] {msg}\n")

    def generate(self, n_rows=500, introduce_nans=True):
        out_dir = self.out_csv.parent
        if not out_dir.exists():
            msg = f'Invalid output directory: {out_dir}'
            self._log_error(msg)
            raise InvalidPathError(msg)

        if not isinstance(n_rows, int) or n_rows <= 0:
            msg = f'n_rows must be a positive integer. Got: {n_rows}'
            self._log_error(msg)
            raise DataGenerationError(msg)

        try:
            age = self.rng.integers(18, 80, size=n_rows)
            income = self.rng.normal(70000, 20000, size=n_rows).clip(15000, None)
            account_balance = self.rng.normal(15000, 8000, size=n_rows).clip(0, None)
            visits_last_month = self.rng.poisson(3, size=n_rows)
            avg_session_minutes = self.rng.normal(12, 6, size=n_rows).clip(0.5, None)

            gender = self.rng.choice(['Male', 'Female', 'Other'], size=n_rows, p=[0.48, 0.48, 0.04])
            product_type = self.rng.choice(['Basic', 'Plus', 'Premium'], size=n_rows, p=[0.5, 0.3, 0.2])

            prob_purchase = (0.2 + 0.000006*(income-30000) + 0.05*(visits_last_month>2).astype(float) +                              0.01*(avg_session_minutes>10).astype(float) + 0.05*(product_type=='Premium').astype(float))
            import numpy as _np
            prob_purchase = _np.clip(prob_purchase, 0.01, 0.95)
            purchased = (self.rng.random(n_rows) < prob_purchase).astype(int)

            df = pd.DataFrame({'age': age, 'income': income.round(2), 'account_balance': account_balance.round(2), 'visits_last_month': visits_last_month, 'avg_session_minutes': avg_session_minutes.round(2), 'gender': gender, 'product_type': product_type, 'purchased': purchased})

            if introduce_nans:
                num_cols = ['age','income','account_balance','visits_last_month','avg_session_minutes']
                for col in num_cols:
                    mask_col = (self.rng.random(n_rows) < 0.006)
                    df.loc[mask_col, col] = _np.nan
                cat_mask = self.rng.random(n_rows) < 0.01
                df.loc[cat_mask, 'gender'] = _np.nan

            df.to_csv(self.out_csv, index=False)
            return df

        except Exception as e:
            msg = f'Unexpected error during generation: {repr(e)}'
            self._log_error(msg)
            raise DataGenerationError(msg) from e
