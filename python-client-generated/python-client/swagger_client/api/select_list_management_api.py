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


class SelectListManagementApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_select_list_using_post(self, **kwargs):  # noqa: E501
        """Create a new select list  # noqa: E501

        Creates a select list using the provided information and returns the select list meta.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_select_list_using_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SelectListDto select_list_dto: The representation of the select list to create
        :return: BaseResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_select_list_using_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.create_select_list_using_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def create_select_list_using_post_with_http_info(self, **kwargs):  # noqa: E501
        """Create a new select list  # noqa: E501

        Creates a select list using the provided information and returns the select list meta.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_select_list_using_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SelectListDto select_list_dto: The representation of the select list to create
        :return: BaseResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select_list_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_select_list_using_post" % key
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
        if 'select_list_dto' in params:
            body_params = params['select_list_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/selectlist', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfSelectListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_using_delete(self, select_list_id, **kwargs):  # noqa: E501
        """Delete a single select list  # noqa: E501

        Deletes a select list with the provided ID. If no such select list exists, this is a no-op.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_using_delete(select_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select_list_id: The unique identifier of the select list (required)
        :return: BaseResponseOfstring
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_using_delete_with_http_info(select_list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_using_delete_with_http_info(select_list_id, **kwargs)  # noqa: E501
            return data

    def delete_using_delete_with_http_info(self, select_list_id, **kwargs):  # noqa: E501
        """Delete a single select list  # noqa: E501

        Deletes a select list with the provided ID. If no such select list exists, this is a no-op.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_using_delete_with_http_info(select_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select_list_id: The unique identifier of the select list (required)
        :return: BaseResponseOfstring
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select_list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'select_list_id' is set
        if self.api_client.client_side_validation and ('select_list_id' not in params or
                                                       params['select_list_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `select_list_id` when calling `delete_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'select_list_id' in params:
            path_params['selectListId'] = params['select_list_id']  # noqa: E501

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
            '/api/v1/selectlist/{selectListId}', 'DELETE',
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

    def get_select_list_using_get(self, select_list_id, **kwargs):  # noqa: E501
        """Retrieve a single select list  # noqa: E501

        Returns a select list that matches the provided ID, or a 404 if no matching select list is found.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_select_list_using_get(select_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select_list_id: The unique identifier of the select list (required)
        :return: BaseResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_select_list_using_get_with_http_info(select_list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_select_list_using_get_with_http_info(select_list_id, **kwargs)  # noqa: E501
            return data

    def get_select_list_using_get_with_http_info(self, select_list_id, **kwargs):  # noqa: E501
        """Retrieve a single select list  # noqa: E501

        Returns a select list that matches the provided ID, or a 404 if no matching select list is found.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_select_list_using_get_with_http_info(select_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str select_list_id: The unique identifier of the select list (required)
        :return: BaseResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select_list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_select_list_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'select_list_id' is set
        if self.api_client.client_side_validation and ('select_list_id' not in params or
                                                       params['select_list_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `select_list_id` when calling `get_select_list_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'select_list_id' in params:
            path_params['selectListId'] = params['select_list_id']  # noqa: E501

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
            '/api/v1/selectlist/{selectListId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfSelectListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_select_lists_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of select lists  # noqa: E501

        Returns a list of select lists associated with the workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_select_lists_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The number of select lists to return, from 1 to 1000; by default, 1000
        :param str cursor: A paging cursor; if included, `limit` is ignored
        :param int offset: The item to start with on the page, greater than or equal to 0; by default, 0
        :return: PagedResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_select_lists_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_select_lists_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_select_lists_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of select lists  # noqa: E501

        Returns a list of select lists associated with the workspace.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_select_lists_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int limit: The number of select lists to return, from 1 to 1000; by default, 1000
        :param str cursor: A paging cursor; if included, `limit` is ignored
        :param int offset: The item to start with on the page, greater than or equal to 0; by default, 0
        :return: PagedResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'cursor', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_select_lists_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
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
            '/api/v1/selectlist', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PagedResponseOfSelectListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_select_list_using_put(self, select_list_dto, select_list_id, **kwargs):  # noqa: E501
        """Update a single select list  # noqa: E501

        Updates the select list with the provided ID with the details provided  in the body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_select_list_using_put(select_list_dto, select_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SelectListDto select_list_dto: The representation of the select list to update (required)
        :param str select_list_id: The unique identifier of the select list (required)
        :return: BaseResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_select_list_using_put_with_http_info(select_list_dto, select_list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_select_list_using_put_with_http_info(select_list_dto, select_list_id, **kwargs)  # noqa: E501
            return data

    def update_select_list_using_put_with_http_info(self, select_list_dto, select_list_id, **kwargs):  # noqa: E501
        """Update a single select list  # noqa: E501

        Updates the select list with the provided ID with the details provided  in the body.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_select_list_using_put_with_http_info(select_list_dto, select_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SelectListDto select_list_dto: The representation of the select list to update (required)
        :param str select_list_id: The unique identifier of the select list (required)
        :return: BaseResponseOfSelectListDto
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['select_list_dto', 'select_list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_select_list_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'select_list_dto' is set
        if self.api_client.client_side_validation and ('select_list_dto' not in params or
                                                       params['select_list_dto'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `select_list_dto` when calling `update_select_list_using_put`")  # noqa: E501
        # verify the required parameter 'select_list_id' is set
        if self.api_client.client_side_validation and ('select_list_id' not in params or
                                                       params['select_list_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `select_list_id` when calling `update_select_list_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'select_list_id' in params:
            path_params['selectListId'] = params['select_list_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'select_list_dto' in params:
            body_params = params['select_list_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['oauth']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/selectlist/{selectListId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BaseResponseOfSelectListDto',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
