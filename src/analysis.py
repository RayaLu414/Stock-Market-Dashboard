"""
analysis.py
Functions for descriptive statistical analysis of stock market data.
"""
import pandas as pd
def calculate_mean(series: pd.Series) -> float:
    """Return the mean of a series of values."""
    return float(series.mean())

def calculate_median(series: pd.Series) -> float:
    """Return the median of a series of values."""
    return float(series.median())

def calculate_variance(series: pd.Series) -> float:
    """Return the variance of a series of values."""
    return float(series.var())

def calculate_standard_deviation(series: pd.Series) -> float:
    """Return the standard deviation of a series of values."""
    return float(series.std())

def calculate_correlation(series1: pd.Series, series2: pd.Series) -> float:
    """Return the correlation between two series of values."""
    return float(series1.corr(series2))

def calculate_skewness(series: pd.Series) -> float:
    """Return the skewness of a series of values."""
    return float(series.skew())

def calculate_kurtosis(series: pd.Series) -> float:
    """Return the kurtosis of a series of values."""
    return float(series.kurt())

def calculate_daily_returns(prices: pd.Series,) -> pd.Series:
    """
    Calculate daily percentage returns from a price series

    Parameters:
    prices: pd.Series
        Time series of historical stock prices.
    
    Returns:
    pd.Series
        Daily percentage returns.
    """
    return prices.pct_change().dropna()

def calculate_moving_average(
    prices: pd.Series,
    window: int,
) -> pd.Series:
    """
    Calculate the rolling moving average of a price series.
    
    Parameters:
    prices : pd.Series
       Time series of historical stock prices.

    window: int
       Number of observations used to calculate the moving average.
       
    Returns:
       Rolling moving average.
    """
    return prices.rolling(window=window).mean()

def calculate_rolling_volatility(
    returns: pd.Series,
    window: int=20,
    ) -> pd.Series:
    """
    Calculate rolling volatility based on the standard deviation of daily return

    Parameter:
    returns: pd.Series
      Time series of daily stock returns

    window: int, default=20
      Number of observations used to calculate rolling volatility.

    Returns:
    pd.Series
      Rolling standard deviation of daily returns.
    """
    return returns.rolling(window=window).std()





