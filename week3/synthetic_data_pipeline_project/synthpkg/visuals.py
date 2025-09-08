import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def save_histogram(series, out_path, bins=30, title=None, xlabel=None):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.hist(series.dropna(), bins=bins)
    ax.set_title(title or f'Histogram of {series.name}')
    ax.set_xlabel(xlabel or series.name)
    ax.set_ylabel('Frequency')
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

def save_bar_counts(series, out_path, title=None, xlabel=None):
    counts = series.value_counts(dropna=False)
    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(counts.index.astype(str), counts.values)
    ax.set_title(title or f'Counts of {series.name}')
    ax.set_xlabel(xlabel or series.name)
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

def save_scatter(x, y, out_path, title=None, xlabel=None, ylabel=None):
    fig, ax = plt.subplots(figsize=(6,4))
    ax.scatter(x, y, s=10)
    ax.set_title(title or 'Scatter Plot')
    ax.set_xlabel(xlabel or getattr(x, 'name', 'x'))
    ax.set_ylabel(ylabel or getattr(y, 'name', 'y'))
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)

def save_corr_heatmap(df, out_path, title='Correlation Heatmap'):
    corr = df.corr(numeric_only=True)
    fig, ax = plt.subplots(figsize=(6,5))
    cax = ax.imshow(corr.values, interpolation='nearest')
    ax.set_title(title)
    ax.set_xticks(range(len(corr.columns)))
    ax.set_yticks(range(len(corr.columns)))
    ax.set_xticklabels(corr.columns, rotation=90)
    ax.set_yticklabels(corr.columns)
    fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
