from swagger_server.models.alpha_vantage_response import AlphaVantageResponse  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501

from alpha_vantage.techindicators import TechIndicators

import config

ti = TechIndicators(key=config.api_key)

def get_adx(symbol, interval, time_period):  # noqa: E501
    """get_adx

    Returns the average directional movement index (ADX) values for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    :type interval: str
    :param time_period: Number of data points used to calculate each ADX value. Positive integers are accepted (e.g., time_period&#x3D;60, time_period&#x3D;200)
    :type time_period: int

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ti.get_adx(symbol=symbol, interval=interval, time_period=time_period)
    return data


def get_aroon(symbol, interval, time_period):  # noqa: E501
    """get_aroon

    Returns AROON indicator values for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    :type interval: str
    :param time_period: Number of data points used to calculate each AROON value. Positive integers are accepted (e.g., time_period&#x3D;60, time_period&#x3D;200)
    :type time_period: int

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ti.get_aroon(symbol=symbol, interval=interval, time_period=time_period)
    return data


def get_bbands(symbol, interval, time_period, series_type):  # noqa: E501
    """get_bbands

    Returns BBANDS indicator values for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    :type interval: str
    :param time_period: Number of data points used to calculate each BBANDS value. Positive integers are accepted (e.g., time_period&#x3D;60, time_period&#x3D;200)
    :type time_period: int
    :param series_type: The desired price type in the time series. Four types are supported: close, open, high, low
    :type series_type: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ti.get_bbands(symbol=symbol, interval=interval, time_period=time_period, series_type=series_type)
    return data


def get_cci(symbol, interval, time_period):  # noqa: E501
    """get_cci

    Returns the commodity channel index (CCI) values for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    :type interval: str
    :param time_period: Number of data points used to calculate each CCI value. Positive integers are accepted (e.g., time_period&#x3D;60, time_period&#x3D;200)
    :type time_period: int

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ti.get_cci(symbol=symbol, interval=interval, time_period=time_period)
    return data

def get_obv(symbol, interval):  # noqa: E501
    """get_obv

    Returns the on balance volume (OBV) values for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min, daily, weekly, monthly
    :type interval: str

    :rtype: AlphaVantageResponse
    """
    data, meta_data = ti.get_obv(symbol=symbol, interval=interval)
    return data
