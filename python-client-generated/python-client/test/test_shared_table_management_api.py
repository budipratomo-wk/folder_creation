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
from swagger_client.api.shared_table_management_api import SharedTableManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSharedTableManagementApi(unittest.TestCase):
    """SharedTableManagementApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.shared_table_management_api.SharedTableManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_shared_table_using_post(self):
        """Test case for create_shared_table_using_post

        Create a new shared table  # noqa: E501
        """
        pass

    def test_delete_shared_table_using_delete(self):
        """Test case for delete_shared_table_using_delete

        Delete a single shared table  # noqa: E501
        """
        pass

    def test_get_shared_table_using_get(self):
        """Test case for get_shared_table_using_get

        Retrieve a single shared table  # noqa: E501
        """
        pass

    def test_list_shared_tables_using_get(self):
        """Test case for list_shared_tables_using_get

        Retrieve a list of shared tables  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
