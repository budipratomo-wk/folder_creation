# coding: utf-8

"""
    Cerebral API

    The Wdata Preparation API allow users to import data sets from their source system, tag, organize, manipulate, share, export, and query against the data  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: scoutteam@workiva.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class SharedTableManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_shared_table_using_post(self, **kwargs):  # noqa: E501
        """Create a new shared table  # noqa: E501

        Creates a shared table instance between the workspace of the request and the workspace provided in the body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_shared_table_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SharedTableDto shared_table_dto: The representation of the shared table to create
        :return: BaseResponseOfSharedTableDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_shared_table_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_shared_table_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_shared_table_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new shared table  # noqa: E501

        Creates a shared table instance between the workspace of the request and the workspace provided in the body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_shared_table_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SharedTableDto shared_table_dto: The representation of the shared table to create
        :return: BaseResponseOfSharedTableDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shared_table_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_shared_table_using_post" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'shared_table_dto' in params:
            body_params = params['shared_table_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sharedtable', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfSharedTableDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_shared_table_using_delete(self, shared_table_id, **kwargs):  # noqa: E501
        """Delete a single shared table  # noqa: E501

        Deletes the linkages between the source and destination of a shared table that matches the provided ID; the actual table itself is left intact. If no such shared table exists, this is a no-op.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_shared_table_using_delete(shared_table_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shared_table_id: The unique identifier of the shared table (required)
        :return: BaseResponseOfstring
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_shared_table_using_delete_with_http_info(shared_table_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_shared_table_using_delete_with_http_info(shared_table_id, **kwargs)  # noqa: E501
            return data

    def delete_shared_table_using_delete_with_http_info(self, shared_table_id, **kwargs):  # noqa: E501
        """Delete a single shared table  # noqa: E501

        Deletes the linkages between the source and destination of a shared table that matches the provided ID; the actual table itself is left intact. If no such shared table exists, this is a no-op.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_shared_table_using_delete_with_http_info(shared_table_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shared_table_id: The unique identifier of the shared table (required)
        :return: BaseResponseOfstring
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shared_table_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_shared_table_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shared_table_id' is set
        if self.api_client.client_side_validation and ('shared_table_id' not in params or
                                                       params['shared_table_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shared_table_id` when calling `delete_shared_table_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shared_table_id' in params:
            path_params['sharedTableId'] = params['shared_table_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sharedtable/{sharedTableId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfstring',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_shared_table_using_get(self, shared_table_id, **kwargs):  # noqa: E501
        """Retrieve a single shared table  # noqa: E501

        Returns a shared table that matches the provided ID, or a 404 if no matching shared table is found.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shared_table_using_get(shared_table_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shared_table_id: The unique identifier of the shared table (required)
        :param bool shared_with_me: If true, returns a shared table with the provided ID that has been shared _to_—rather than from—the workspace of the request.
        :return: BaseResponseOfSharedTableDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_shared_table_using_get_with_http_info(shared_table_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_shared_table_using_get_with_http_info(shared_table_id, **kwargs)  # noqa: E501
            return data

    def get_shared_table_using_get_with_http_info(self, shared_table_id, **kwargs):  # noqa: E501
        """Retrieve a single shared table  # noqa: E501

        Returns a shared table that matches the provided ID, or a 404 if no matching shared table is found.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_shared_table_using_get_with_http_info(shared_table_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shared_table_id: The unique identifier of the shared table (required)
        :param bool shared_with_me: If true, returns a shared table with the provided ID that has been shared _to_—rather than from—the workspace of the request.
        :return: BaseResponseOfSharedTableDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shared_table_id', 'shared_with_me']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_shared_table_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shared_table_id' is set
        if self.api_client.client_side_validation and ('shared_table_id' not in params or
                                                       params['shared_table_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `shared_table_id` when calling `get_shared_table_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'shared_table_id' in params:
            path_params['sharedTableId'] = params['shared_table_id']  # noqa: E501

        query_params = []
        if 'shared_with_me' in params:
            query_params.append(('sharedWithMe', params['shared_with_me']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sharedtable/{sharedTableId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfSharedTableDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_shared_tables_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of shared tables  # noqa: E501

        Returns a list of shared tables associated with the workspace of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_shared_tables_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str table_id: The unique table identifier associated with the shared table
        :param bool shared_with_me: If true, returns a list of tables that have been shared _to_ it rather than from it. The entities contain both the shared table entity _and_ the table being shared. If true, `tableId` is ignored.
        :param int limit: The number of shared files to return, from 1 to 1000; by default, 1000
        :param str cursor: A paging cursor; if included, `limit` is ignored
        :param int offset: The item to start with on the page, greater than or equal to 0; by default, 0
        :return: PagedResponseOfSharedTableDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_shared_tables_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_shared_tables_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_shared_tables_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of shared tables  # noqa: E501

        Returns a list of shared tables associated with the workspace of the request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_shared_tables_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str table_id: The unique table identifier associated with the shared table
        :param bool shared_with_me: If true, returns a list of tables that have been shared _to_ it rather than from it. The entities contain both the shared table entity _and_ the table being shared. If true, `tableId` is ignored.
        :param int limit: The number of shared files to return, from 1 to 1000; by default, 1000
        :param str cursor: A paging cursor; if included, `limit` is ignored
        :param int offset: The item to start with on the page, greater than or equal to 0; by default, 0
        :return: PagedResponseOfSharedTableDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['table_id', 'shared_with_me', 'limit', 'cursor', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_shared_tables_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 1000):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_shared_tables_using_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_shared_tables_using_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'table_id' in params:
            query_params.append(('tableId', params['table_id']))  # noqa: E501
        if 'shared_with_me' in params:
            query_params.append(('sharedWithMe', params['shared_with_me']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'cursor' in params:
            query_params.append(('cursor', params['cursor']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/sharedtable', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponseOfSharedTableDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)