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
from swagger_client.api.connection_management_api import ConnectionManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConnectionManagementApi(unittest.TestCase):
    """ConnectionManagementApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.connection_management_api.ConnectionManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_connection_using_get(self):
        """Test case for get_connection_using_get

        Get connection details  # noqa: E501
        """
        pass

    def test_get_refresh_batch_status_using_get(self):
        """Test case for get_refresh_batch_status_using_get

        Gets the status of a batch refresh  # noqa: E501
        """
        pass

    def test_get_refresh_status_using_get(self):
        """Test case for get_refresh_status_using_get

        Get connection refresh status  # noqa: E501
        """
        pass

    def test_list_connections_using_get(self):
        """Test case for list_connections_using_get

        List connections  # noqa: E501
        """
        pass

    def test_refresh_batch_using_post(self):
        """Test case for refresh_batch_using_post

        Refresh batch of connections  # noqa: E501
        """
        pass

    def test_refresh_connection_using_post(self):
        """Test case for refresh_connection_using_post

        Refresh connection  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()