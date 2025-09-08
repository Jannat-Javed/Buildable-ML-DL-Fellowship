import numpy as np

def mean(arr):
    arr = np.asarray(arr, dtype=float)
    return float(np.nanmean(arr))

def median(arr):
    arr = np.asarray(arr, dtype=float)
    return float(np.nanmedian(arr))

def std(arr):
    arr = np.asarray(arr, dtype=float)
    return float(np.nanstd(arr, ddof=0))
