"""
Visualization utilities for the Statistical Stock Market Dashboard.
This module provides reusable functions for creating charts based on historical stock market data.
Each function is responsible foe generating a specific type of visualization,
allowing the plotting logic to remain separate from data processing and statistical analysis.

The charts in this module are intended to support exploratory analysis and dashboard development 
by visualizing stock prices,trends,returns,volatility and other commonly used financial metrics.
"""

import matplotlib.pyplot as plt
import pandas as pd

def plot_stock_price(
    df: pd.DataFrame,
    ticker: str,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """
    Plot the historical closing price of a stock.
    This function creates a line chart showing the daily closing prices contained
    in the input DataFrame. If an existing Matplotlib Axes object is provided,
    the chart is drawn on the Axes; otherwise, a new figure and Axes are created.

    Parameters:
    df : pd.DataFrame
        DataFrame containing historical stock price data. The DataFrame should use dates
        as the index and include a "Close" column
    ticker : str
        Stock ticker symbol used as the chart title
    ax : matplotlib.axes.Axes, optional
        Existing Axes object to plot on. If None, a new figure and Axes are created automatically.
    
    Returns:
        matplotlib.axes.Axes
        The Axes object containg the completed plot.
    """
    if ax is None:
        _, ax = plt.subplots(figsize=(12, 6))
    
    ax.plot(
        df.index,
        df["Close"],
        label="Closing Price",
        linewidth=2,
    )
    
    ax.set_title(f"{ticker} Stock Price")
    ax.set_xlabel("Date")
    ax.set_ylabel("Price(USD)")
    ax.grid(True)
    ax.legend()
    
    ax.figure.tight_layout()
    return ax

def plot_daily_returns(
    returns: pd.Series,
    ticker:str,
    ax: plt.Axes | None = None,
) -> plt.Axes:
    """
    Plot the daily percentage returns of a stock.
    This function creates a time-series line charts showing the daily 
    percentage returns of a stock. A horizontal reference line at zero
    return is included to distinguish positive and negative performance.

    Parameters:
    returns: pd.Series,
       Time series of daily stock returns. The Series should use datas as the index.
    
    ticker : str
       Stock ticker symbol used as the chart title

    ax: matplotlib.axes.Axes, optional
       Existing Axes object to plot on. If None, a new figure and 
       Axes are created automatimatically.

    Returns:
    matplotlib.axes.Axes
       The Axes object containng the completed plot.
    """

    if ax is None:
        _, ax = plt.subplots(figsize=(12,6))

    ax.plot(
        returns.index,
        returns * 100,
        label="Daily Return",
        linewidth=1,
    )

    ax.axhline(
        y=0,
        linestyle="--",
        linewidth=1,
        label="Zero Return",
    )

    ax.set_title(f"{ticker} Daily Returns")
    ax.set_xlabel("Date")
    ax.set_ylabel("Daily Return(%)")

    ax.grid(True)
    ax.legend()

    ax.figure.tight_layout()

    return ax


def plot_moving_average(
    prices: pd.Series,
    moving_averages: dict[int, pd.Series]
    ticker: str,
    ax: plt.Axes | None = None,
) -> plt.Axes:
"""
Plot historical stock prices together with moving averages.

This function creates a line chart showing the historical 
closing price of a stock and one or more pre-calculated moving averages.
Moving averages help smooth short-term price fluctuations 
and higlight underlying price trends.

Parameters:
prices: pd.Series
   Time series of historical closing prices. The Series should use dates as the index.

moving_averages: dic[int, pd.Series]
   Dictionary mapping each moving-average window to its calculated moving-average Series.
   For example:
   {
   20: moving_average_20,
   30: moving_average_30
   }

ticker: str
   Stock ticker symbol as the chart title.

ax: matplotlib.axes.Axes, optional
   Existing Axes object to plot on. If None, a new figure and Axes are created automatically.

Returns:
matplotlib.axes.Axes
   The Axes object containing the complete plot.
"""
if ax is None:
    _, ax = plt.subplots(figsize=(12,6))

ax.plot(
    prices.index,
    prices,
    label="Closing Price",
    linewidth=2,
)

for window, moving_average in moving_averages.items():
    ax.plot(
        moving_average.index,
        moving_average,
        label=f"{window}-Day Moving Average",
        linewidth=1.5,
    )

ax.set_title(f"{ticker} Price and Moving Averages")
ax.set_xlabel("Date")
ax.set_ylabel("Price (USD)")

ax.grid(True)
ax.legend()

ax.figure.tight_layout()

return ax

def plot_return_distribution(
    returns: pd.Series,
    ticker: str,
    ax: plt.Axes | None=None,
) -> plt.Axes:
"""
plot the distribution of daily stock returns.

This is function creats a histogram showing the distribution of 
daily return. The distribution helps visualize the frequency,
dispersion, and shape of the stock's daily performance.

Parameters:
returns: pd.Series
   Time series of dailt stock returns.

ticker: str
   Stock ticker symbol used as the chart title.

ax: matplotlib.axes.Axes, optional
   Existing Axes object to plot on. If None, a new figure and Axes are created automatically.
"""
if ax is None:
    _, ax = plt.subplots(figsize=(12,6))

ax.hist(
    returns * 100,
    bins=50,
    alpha=0.7,
    edgecolor="black",
)

ax.axvline(
    returns.mean() * 100,
    linestyle="--",
    linewidth=2,
    label=f"Mean: {returns.mean() * 100: .2f}%",
)

ax.set_title(f"{ticker} Daily Return Distribution")
ax.set_xlabel("Daily Return(%)")
ax.set_ylabel("Frequency")

ax.grid(True)
ax.legend()

ax.figure.tight_layout()

return ax

def plot_rolling_volatility(
    rolling_volatility: pd.Series,
    ticker: str,
    window: int = 20,
    ax: plt.Axes | None = None,
) -> plt.Axes:
"""
Plot the rolling volatility of a stock.

This function visualizes the time-varying volatility of a stock
based on the rolling standard deviation of daily returns. It helps
identify periods of relatively high and low market risk. 

Parameters:
rolling_volatility : pd.Series
   Time series of rolling volatility calculated from daily returns.

ticker: str
   Stock ticker symbol used as the chart title

window : int, default = 20
   Rolling window used to calculate volatility.

ax : matplotlib.axes.Axes, optional
   Existing Axes object to plot on. If None, a new figure and Axes are created automatically.

Returns
matplotlib.axes.Axes
   The Axes object containing the completed plot.
"""
if ax is None:
    _, ax = plt.subplots(figsize=(12,6))

ax.plot(
    rolling_volatility.index,
    rolling_volatility * 100,
    label=f"{window} - Day Rolling Volatility",
    linewidth=2
)

ax.set_title(f"{ticker} Rolling Volatility")
ax.set_xlabel("Date")
ax.set_ylabel("Volatility (%)")

ax.grid(True)
ax.legend()

ax.figure.tight_layout()

return ax