import numpy as np
import pandas as pd

def augment_df(df, numeric_cols, target_col=None, scale=1.0, noise_frac=0.02, target_size_factor=2.0, random_state=42):
    rng = np.random.default_rng(random_state)
    n_original = len(df)
    n_target = int(np.ceil(target_size_factor * n_original))
    idx = rng.integers(low=0, high=n_original, size=n_target)
    df_aug = df.iloc[idx].copy().reset_index(drop=True)
    for col in numeric_cols:
        col_std = df[col].std(ddof=0)
        noise = rng.normal(loc=0.0, scale=max(1e-12, noise_frac * col_std * scale), size=len(df_aug))
        df_aug[col] = df_aug[col].astype(float) + noise
    return df_aug
