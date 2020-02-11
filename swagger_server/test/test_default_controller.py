# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.alpha_vantage_response import AlphaVantageResponse  # noqa: E501
from swagger_server.models.data_to_predict import DataToPredict  # noqa: E501
from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.model_info import ModelInfo  # noqa: E501
from swagger_server.models.predict_response import PredictResponse  # noqa: E501
from swagger_server.models.train_data import TrainData  # noqa: E501
from swagger_server.models.train_started_success import TrainStartedSuccess  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_delete_delete(self):
        """Test case for delete_delete

        Deletes a model from storage
        """
        query_string = [('modelId', 'modelId_example')]
        response = self.client.open(
            '/delete',
            method='DELETE',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_adx(self):
        """Test case for get_adx

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example'),
                        ('time_period', 56)]
        response = self.client.open(
            '/get_adx',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_aroon(self):
        """Test case for get_aroon

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example'),
                        ('time_period', 56)]
        response = self.client.open(
            '/get_aroon',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_bbands(self):
        """Test case for get_bbands

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example'),
                        ('time_period', 56),
                        ('series_type', 'series_type_example')]
        response = self.client.open(
            '/get_bbands',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_cci(self):
        """Test case for get_cci

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example'),
                        ('time_period', 56)]
        response = self.client.open(
            '/get_cci',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_daily(self):
        """Test case for get_daily

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('outputsize', 'outputsize_example')]
        response = self.client.open(
            '/get_daily',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_daily_adjusted(self):
        """Test case for get_daily_adjusted

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('outputsize', 'outputsize_example')]
        response = self.client.open(
            '/get_daily_adjusted',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_intraday(self):
        """Test case for get_intraday

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example'),
                        ('outputsize', 'outputsize_example')]
        response = self.client.open(
            '/get_intraday',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_monthly(self):
        """Test case for get_monthly

        
        """
        query_string = [('symbol', 'symbol_example')]
        response = self.client.open(
            '/get_monthly',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_monthly_adjusted(self):
        """Test case for get_monthly_adjusted

        
        """
        query_string = [('symbol', 'symbol_example')]
        response = self.client.open(
            '/get_monthly_adjusted',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_obv(self):
        """Test case for get_obv

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example')]
        response = self.client.open(
            '/get_obv',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_quote_endpoint(self):
        """Test case for get_quote_endpoint

        
        """
        query_string = [('symbol', 'symbol_example')]
        response = self.client.open(
            '/get_quote_endpoint',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_symbol(self):
        """Test case for get_symbol

        
        """
        query_string = [('keywords', 'keywords_example')]
        response = self.client.open(
            '/get_symbol',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_weekly(self):
        """Test case for get_weekly

        
        """
        query_string = [('symbol', 'symbol_example')]
        response = self.client.open(
            '/get_weekly',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_weekly_adjusted(self):
        """Test case for get_weekly_adjusted

        
        """
        query_string = [('symbol', 'symbol_example')]
        response = self.client.open(
            '/get_weekly_adjusted',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_models_get(self):
        """Test case for list_models_get

        Reruns list of models from model storage
        """
        response = self.client.open(
            '/list_models',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_predict(self):
        """Test case for predict

        Predict value
        """
        data_to_predict = DataToPredict()
        response = self.client.open(
            '/predict',
            method='POST',
            data=json.dumps(data_to_predict),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_train_post(self):
        """Test case for train_post

        Trains a new model
        """
        trainData = TrainData()
        response = self.client.open(
            '/train',
            method='POST',
            data=json.dumps(trainData),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
