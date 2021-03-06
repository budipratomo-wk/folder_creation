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
from swagger_client.api.tag_management_api import TagManagementApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTagManagementApi(unittest.TestCase):
    """TagManagementApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.tag_management_api.TagManagementApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_tag_using_post(self):
        """Test case for create_tag_using_post

        Create a new tag  # noqa: E501
        """
        pass

    def test_delete_tag_using_delete(self):
        """Test case for delete_tag_using_delete

        Delete a single tag  # noqa: E501
        """
        pass

    def test_list_tags_using_get(self):
        """Test case for list_tags_using_get

        Retrieve a list of tags  # noqa: E501
        """
        pass

    def test_update_tag_using_put(self):
        """Test case for update_tag_using_put

        Update a single tag  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
