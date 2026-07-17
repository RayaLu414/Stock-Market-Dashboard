"""
analysis.py
Functions for descriptive statistical analysis of stock market data.
"""
import pandas as pd
def calculate_mean(series: pd.Series) -> float:
    """Return the mean of a series of values."""
    return float(series.mean())

def calculate_median(series: pd.series) -> float:
    """Return the median of a series of values."""
    return float(series.median())

def calculate_variance(series: pd.series) -> float:
    """Return the variance of a series of values."""
    return float(series.var())

def calculate_standard_deviation(series: pd.series) -> float:
    """Return the standard deviation of a series of values."""
    return float(series.std())

def calculate_correlation(series1: pd.series, series2: pd.series) -> float:
    """Return the correlation between two series of values."""
    return float(series1.corr(series2))

def calculate_regression(series1: pd.series, series2: pd.series) -> float:
    """Return the regression of a series of values."""
    return float(series1.regress(series2))

def calculate_skewness(series: pd.series) -> float:
    """Return the skewness of a series of values."""
    return float(series.skew())

def calculate_kurtosis(series: pd.series) -> float:
    """Return the kurtosis of a series of values."""
    return float(series.kurt())