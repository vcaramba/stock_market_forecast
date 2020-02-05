# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.error_response import ErrorResponse  # noqa: E501
from swagger_server.models.timeseries_response import TimeseriesResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestDefaultController(BaseTestCase):
    """DefaultController integration test stubs"""

    def test_get_timeseries_data(self):
        """Test case for get_timeseries_data

        
        """
        query_string = [('symbol', 'symbol_example'),
                        ('interval', 'interval_example')]
        response = self.client.open(
            '//get_timeseries',
            method='GET',
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
