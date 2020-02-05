import connexion
import six
from alpha_vantage.timeseries import TimeSeries

import config
from swagger_server import util
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.timeseries_response import TimeseriesResponse  # noqa: E501


def get_timeseries_data(symbol, interval):  # noqa: E501
    """get_timeseries_data

    Returns stock timeseries data for requested company # noqa: E501

    :param symbol: The symbol of company
    :type symbol: str
    :param interval: Time interval between two consecutive data points in the time series. The following values are supported: 1min, 5min, 15min, 30min, 60min
    :type interval: str

    :rtype: TimeseriesResponse
    """
    ts = TimeSeries(key=config.api_key)
    # Get json object with the intraday data and another with  the call's metadata
    data, meta_data = ts.get_intraday(symbol=symbol, interval=interval)
    return data
