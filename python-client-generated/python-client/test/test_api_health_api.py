# coding: utf-8

"""
    Cerebral API

    The Wdata Preparation API allow users to import data sets from their source system, tag, organize, manipulate, share, export, and query against the data  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: scoutteam@workiva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.api_health_api import APIHealthApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAPIHealthApi(unittest.TestCase):
    """APIHealthApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.api_health_api.APIHealthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_health_check_using_get(self):
        """Test case for health_check_using_get

        Health check  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
