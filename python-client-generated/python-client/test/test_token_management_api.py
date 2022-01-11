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
from swagger_client.api.token_management_api import TokenManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTokenManagementApi(unittest.TestCase):
    """TokenManagementApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.token_management_api.TokenManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_token_using_post(self):
        """Test case for create_token_using_post

        Create a new token  # noqa: E501
        """
        pass

    def test_download_file_using_get1(self):
        """Test case for download_file_using_get1

        Download a single file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
