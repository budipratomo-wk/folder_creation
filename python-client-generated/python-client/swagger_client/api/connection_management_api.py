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


class ConnectionManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_connection_using_get(self, connection_id, **kwargs):  # noqa: E501
        """Get connection details  # noqa: E501

        Returns details about a specific connection, based on its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection_using_get(connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connection_id: The ID of the connection to return details about (required)
        :return: BaseResponseOfConnectionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_connection_using_get_with_http_info(connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_connection_using_get_with_http_info(connection_id, **kwargs)  # noqa: E501
            return data

    def get_connection_using_get_with_http_info(self, connection_id, **kwargs):  # noqa: E501
        """Get connection details  # noqa: E501

        Returns details about a specific connection, based on its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_connection_using_get_with_http_info(connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connection_id: The ID of the connection to return details about (required)
        :return: BaseResponseOfConnectionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_connection_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_id' is set
        if self.api_client.client_side_validation and ('connection_id' not in params or
                                                       params['connection_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `connection_id` when calling `get_connection_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

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
            '/api/v1/connections/{connectionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfConnectionDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_refresh_batch_status_using_get(self, batch_id, **kwargs):  # noqa: E501
        """Gets the status of a batch refresh  # noqa: E501

        Returns details about a specific batch refresh, based on its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_batch_status_using_get(batch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_id: The ID of the batch to return details about (required)
        :return: BaseResponseOfRefreshBatchDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_refresh_batch_status_using_get_with_http_info(batch_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_refresh_batch_status_using_get_with_http_info(batch_id, **kwargs)  # noqa: E501
            return data

    def get_refresh_batch_status_using_get_with_http_info(self, batch_id, **kwargs):  # noqa: E501
        """Gets the status of a batch refresh  # noqa: E501

        Returns details about a specific batch refresh, based on its ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_batch_status_using_get_with_http_info(batch_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str batch_id: The ID of the batch to return details about (required)
        :return: BaseResponseOfRefreshBatchDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['batch_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_refresh_batch_status_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'batch_id' is set
        if self.api_client.client_side_validation and ('batch_id' not in params or
                                                       params['batch_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `batch_id` when calling `get_refresh_batch_status_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'batch_id' in params:
            path_params['batchId'] = params['batch_id']  # noqa: E501

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
            '/api/v1/connections/batch/refresh/{batchId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfRefreshBatchDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_refresh_status_using_get(self, connection_id, **kwargs):  # noqa: E501
        """Get connection refresh status  # noqa: E501

        Returns details about a specific connection refresh status, based on its ID. To retrieve details about a specific refresh, provide its 'jobId'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_status_using_get(connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connection_id: The ID of the connection to return details about (required)
        :param str job_id: The ID of the job running for a connection
        :return: BaseResponseOfConnectionRunDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_refresh_status_using_get_with_http_info(connection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_refresh_status_using_get_with_http_info(connection_id, **kwargs)  # noqa: E501
            return data

    def get_refresh_status_using_get_with_http_info(self, connection_id, **kwargs):  # noqa: E501
        """Get connection refresh status  # noqa: E501

        Returns details about a specific connection refresh status, based on its ID. To retrieve details about a specific refresh, provide its 'jobId'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_refresh_status_using_get_with_http_info(connection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connection_id: The ID of the connection to return details about (required)
        :param str job_id: The ID of the job running for a connection
        :return: BaseResponseOfConnectionRunDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_id', 'job_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_refresh_status_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_id' is set
        if self.api_client.client_side_validation and ('connection_id' not in params or
                                                       params['connection_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `connection_id` when calling `get_refresh_status_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []
        if 'job_id' in params:
            query_params.append(('jobId', params['job_id']))  # noqa: E501

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
            '/api/v1/connections/{connectionId}/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfConnectionRunDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_connections_using_get(self, **kwargs):  # noqa: E501
        """List connections  # noqa: E501

        A pageable endpoint to list data connections between features of the Workiva platform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connections_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_type: The type of file or item the connection pulls data from
        :param str destination_type: The type of file or item the connection sends data to
        :param str source_id: The ID of the file or item the connection pulls data from
        :param str destination_id: The ID of the file or item the connection sends data to
        :param int limit: The number of connections to return, from 1 to 1000; by default, 1000
        :param str cursor: A paging cursor; if included, `limit` is ignored
        :param int offset: The item to start with on the page, greater than or equal to 0; by default, 0
        :return: PagedResponseOfConnectionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_connections_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_connections_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_connections_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """List connections  # noqa: E501

        A pageable endpoint to list data connections between features of the Workiva platform  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_connections_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str source_type: The type of file or item the connection pulls data from
        :param str destination_type: The type of file or item the connection sends data to
        :param str source_id: The ID of the file or item the connection pulls data from
        :param str destination_id: The ID of the file or item the connection sends data to
        :param int limit: The number of connections to return, from 1 to 1000; by default, 1000
        :param str cursor: A paging cursor; if included, `limit` is ignored
        :param int offset: The item to start with on the page, greater than or equal to 0; by default, 0
        :return: PagedResponseOfConnectionDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['source_type', 'destination_type', 'source_id', 'destination_id', 'limit', 'cursor', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_connections_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 1000):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_connections_using_get`, must be a value less than or equal to `1000`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `list_connections_using_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'source_type' in params:
            query_params.append(('sourceType', params['source_type']))  # noqa: E501
        if 'destination_type' in params:
            query_params.append(('destinationType', params['destination_type']))  # noqa: E501
        if 'source_id' in params:
            query_params.append(('sourceId', params['source_id']))  # noqa: E501
        if 'destination_id' in params:
            query_params.append(('destinationId', params['destination_id']))  # noqa: E501
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
            '/api/v1/connections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponseOfConnectionDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_batch_using_post(self, refresh_connection_dtos, **kwargs):  # noqa: E501
        """Refresh batch of connections  # noqa: E501

        Refreshes multiple connections at once, based on their IDs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_batch_using_post(refresh_connection_dtos, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RefreshConnectionDto] refresh_connection_dtos: refreshConnectionDtos (required)
        :return: BaseResponseOfRefreshBatchDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_batch_using_post_with_http_info(refresh_connection_dtos, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_batch_using_post_with_http_info(refresh_connection_dtos, **kwargs)  # noqa: E501
            return data

    def refresh_batch_using_post_with_http_info(self, refresh_connection_dtos, **kwargs):  # noqa: E501
        """Refresh batch of connections  # noqa: E501

        Refreshes multiple connections at once, based on their IDs  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_batch_using_post_with_http_info(refresh_connection_dtos, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param list[RefreshConnectionDto] refresh_connection_dtos: refreshConnectionDtos (required)
        :return: BaseResponseOfRefreshBatchDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['refresh_connection_dtos']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_batch_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'refresh_connection_dtos' is set
        if self.api_client.client_side_validation and ('refresh_connection_dtos' not in params or
                                                       params['refresh_connection_dtos'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `refresh_connection_dtos` when calling `refresh_batch_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'refresh_connection_dtos' in params:
            body_params = params['refresh_connection_dtos']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/connections/batch/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfRefreshBatchDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def refresh_connection_using_post(self, connection_id, refresh_connection_dto, **kwargs):  # noqa: E501
        """Refresh connection  # noqa: E501

        Refreshes a specific connection, based on its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_connection_using_post(connection_id, refresh_connection_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connection_id: The ID of the connection to refresh (required)
        :param RefreshConnectionDto refresh_connection_dto: refreshConnectionDto (required)
        :return: BaseResponseOfConnectionRunDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.refresh_connection_using_post_with_http_info(connection_id, refresh_connection_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.refresh_connection_using_post_with_http_info(connection_id, refresh_connection_dto, **kwargs)  # noqa: E501
            return data

    def refresh_connection_using_post_with_http_info(self, connection_id, refresh_connection_dto, **kwargs):  # noqa: E501
        """Refresh connection  # noqa: E501

        Refreshes a specific connection, based on its ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.refresh_connection_using_post_with_http_info(connection_id, refresh_connection_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str connection_id: The ID of the connection to refresh (required)
        :param RefreshConnectionDto refresh_connection_dto: refreshConnectionDto (required)
        :return: BaseResponseOfConnectionRunDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['connection_id', 'refresh_connection_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method refresh_connection_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'connection_id' is set
        if self.api_client.client_side_validation and ('connection_id' not in params or
                                                       params['connection_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `connection_id` when calling `refresh_connection_using_post`")  # noqa: E501
        # verify the required parameter 'refresh_connection_dto' is set
        if self.api_client.client_side_validation and ('refresh_connection_dto' not in params or
                                                       params['refresh_connection_dto'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `refresh_connection_dto` when calling `refresh_connection_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'connection_id' in params:
            path_params['connectionId'] = params['connection_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'refresh_connection_dto' in params:
            body_params = params['refresh_connection_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/connections/{connectionId}/refresh', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfConnectionRunDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)