"""
data_loader.py
--------------
Functions for downloading and preparing stock market data.
"""

import pandas as pd
import yfinance as yf


def get_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Download historical stock price data for a given ticker.

    Parameters
    ----------
    ticker : str
        Stock ticker symbol (e.g. "AAPL" for Apple, "MSFT" for Microsoft).
    start_date : str
        Start date in "YYYY-MM-DD" format (e.g. "2020-01-01").
    end_date : str
        End date in "YYYY-MM-DD" format (e.g. "2024-12-31").

    Returns
    -------
    pd.DataFrame
        A cleaned DataFrame with columns:
        Date, Open, High, Low, Close, Volume
    """
    # Download data from Yahoo Finance
    # yfinance returns a DataFrame indexed by trading date
    raw_data = yf.download(
        tickers=ticker,
        start=start_date,
        end=end_date,
        progress=False,  # hide the download progress bar
    )

    # Raise a clear error if no data was returned
    if raw_data.empty:
        raise ValueError(
            f"No data found for ticker '{ticker}' "
            f"between {start_date} and {end_date}."
        )

    # yfinance sometimes returns multi-level column names for a single ticker
    # Flatten them so we get simple names like "Open", "Close", etc.
    if isinstance(raw_data.columns, pd.MultiIndex):
        raw_data.columns = raw_data.columns.get_level_values(0)

    # Move the date index into a regular column called "Date"
    clean_data = raw_data.reset_index()

    # Keep only the columns we need for analysis
    columns_to_keep = ["Date", "Open", "High", "Low", "Close", "Volume"]
    clean_data = clean_data[columns_to_keep]

    # Remove rows with missing values
    clean_data = clean_data.dropna()

    # Sort oldest to newest (helpful for charts and calculations)
    clean_data = clean_data.sort_values("Date").reset_index(drop=True)

    return clean_data
