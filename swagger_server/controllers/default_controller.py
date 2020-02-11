import connexion
import six

from swagger_server.models.alpha_vantage_response import AlphaVantageResponse  # noqa: E501
from swagger_server.models.data_to_predict import DataToPredict  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.model_info import ModelInfo  # noqa: E501
from swagger_server.models.predict_response import PredictResponse  # noqa: E501
from swagger_server.models.train_data import TrainData  # noqa: E501
from swagger_server.models.train_started_success import TrainStartedSuccess  # noqa: E501
from swagger_server import util

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators

import config

ts = TimeSeries(key=config.api_key)
ti = TechIndicators(key=config.api_key, output_format='pandas')


def delete_delete(modelId):  # noqa: E501
    """Deletes a model from storage

     # noqa: E501

    :param modelId: id of the model to delete
    :type modelId: str

    :rtype: None
    """
    return 'do some magic!'


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


def list_models_get():  # noqa: E501
    """Reruns list of models from model storage

     # noqa: E501


    :rtype: List[ModelInfo]
    """
    return 'do some magic!'


def predict(data_to_predict):  # noqa: E501
    """Predict entities from text

     # noqa: E501

    :param data_to_predict: List of texts to perform prediction on
    :type data_to_predict: dict | bytes

    :rtype: List[PredictResponse]
    """
    if connexion.request.is_json:
        data_to_predict = DataToPredict.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def train_post(trainData):  # noqa: E501
    """Trains a new model

     # noqa: E501

    :param trainData: Neural network training parameters and training data description
    :type trainData: dict | bytes

    :rtype: TrainStartedSuccess
    """
    if connexion.request.is_json:
        trainData = TrainData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
