import connexion
import six

from swagger_server.models.alpha_vantage_response import AlphaVantageResponse  # noqa: E501

from swagger_server.models.error_response import ErrorResponse  # noqa: E501

from swagger_server import util

from alpha_vantage.timeseries import TimeSeries
import config

ts = TimeSeries(key=config.api_key)


def get_daily(symbol, outputsize):  # noqa: E501
    """get_daily

    Returns daily timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param outputsize: The outputsize. Supported values: compact, full
    :type outputsize: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_daily(symbol=symbol, outputsize=outputsize)
    return data


def get_daily_adjusted(symbol, outputsize):  # noqa: E501
    """get_daily_adjusted

    Returns adjusted daily timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param outputsize: The outputsize. Supported values: compact, full
    :type outputsize: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_daily_adjusted(symbol=symbol, outputsize=outputsize)
    return data


def get_intraday(symbol, interval, outputsize):  # noqa: E501
    """get_intraday

    Returns intraday timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
    :type interval: str
    :param outputsize: The outputsize. Supported values: compact, full
    :type outputsize: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_intraday(symbol=symbol, interval=interval, outputsize=outputsize)
    return data


def get_monthly(symbol):  # noqa: E501
    """get_monthly

    Returns monthly timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_monthly(symbol=symbol)
    return data


def get_monthly_adjusted(symbol):  # noqa: E501
    """get_monthly_adjusted

    Returns adjusted monthly timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_monthly_adjusted(symbol=symbol)
    return data




def get_quote_endpoint(symbol):  # noqa: E501
    """get_quote_endpoint

    Returns the latest price and volume information data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str

    :rtype: AlphaVantageResponse
    """
    return ts.get_quote_endpoint(symbol)


def get_symbol(keywords):  # noqa: E501
    """get_symbol

    Returns suggested company symbol(s) based on search # noqa: E501

    :param keywords: The keywords
    :type keywords: str

    :rtype: AlphaVantageResponse
    """
    return ts.get_symbol_search(keywords)



def get_weekly(symbol):  # noqa: E501
    """get_weekly

    Returns weekly timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_weekly(symbol=symbol)
    return data


def get_weekly_adjusted(symbol):  # noqa: E501
    """get_weekly_adjusted

    Returns adjusted weekly timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ts.get_weekly_adjusted(symbol=symbol)
    return data
