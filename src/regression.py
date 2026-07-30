from dataclasses import dataclass

import pandas as pd
from scipy.stats import linregress

@dataclass
class RegressionResult:
    """
    Store the result of a stock-market return regression.

    Attrbutes:
    alpha : float
       Estimate regression intercept. It represents the expected stock return
       when market return is zero.
    beta : float
       Estimated market sensitivity of the stock. It reprsents the expected change
       in stock return associated with a one-unit change in market return.
    r_square : float
       Proportion of variation in stock returns explained by market returns.
    p_value : float
       Two_sided p-calue for the hypothesis test that the regression slope is equal to zero
    standard_error : float
       Standard error of the estimated rehression slope.
    predicted_returns : pandas.Series
       Stock returns predicted by the regression model.
    residuals : pandas.Series
       Differences between actual and predicted stock returns.
    """

    alpha : float
    beta : float
    r_squared : float
    p_value : float
    standard_error : float
    predicted_returns : pd.Series
    residuals : pd.Series


def run_market_regression(
    stock_returns : pd.Series,
    market_returns : pd.Series,
    ) -> RegressionResult:
    """
    Run a linear regression of stock returns on market returns.

    The regression model is:
       stock_return = alpha + beta * market_return + error
    The input return series are aligned by date before the regression is estimated.
    Dates with missing values in either series are removed.

    Parameters
    ------
    stock_returns : pd.Series
       Historical returns for an individual stock. The Series index should contain dates. 
    market_returns : pd.Series
       Historical returns for a market benchmark. The Series index should contain dates.
    
    Returns
    ------
    RegressionResult
       A strctured object containing the estimated alpha, beta, R_squared, p_value, 
       standard_error, predicted returns, and residuals.
    
    Raises
    ------
    ValueError
       If the input series so not contain enough aligned observations to estimate the regression.
    """

    aligned_returns = pd.concat(
      [
        stock_returns.rename("stock_return"),
        market_returns.rename("market_return"),
      ],
      axis=1,
      join="inner",
    ).dropna()

    if len(aligned_returns) < 3:
        raise ValueError(
            "At Least three aligned return observations are required"
            "to run the regression."
        )

    regression = linregress(
        x=aligned_returns["market_return"],
        y=aligned_returns["stock_return"],
    )

    predicted_returns = pd.Series(
        regression.intercept
        + regression.slope * aligned_returns["market_return"],
        index=aligned_returns.index,
        name="predicted_return"
    )

    residuals = (
        aligned_returns["stock_return"] - predicted_returns
    ).rename("residual")

    return RegressionResult(
        alpha=float(regression.intercept),
        beta=float(regression.slope),
        r_squared=float(regression.rvalue**2),
        p_value=float(regression.pvalue),
        standard_error=float(regression.stderr),
        predicted_returns=predicted_returns,
        residuals=residuals,
    )

