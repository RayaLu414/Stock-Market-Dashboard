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