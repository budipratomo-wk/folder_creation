# swagger_client.PivotViewManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_pivot_view_using_post**](PivotViewManagementApi.md#create_pivot_view_using_post) | **POST** /api/v1/pivotview | Create a new pivot view
[**delete_pivot_view_using_delete**](PivotViewManagementApi.md#delete_pivot_view_using_delete) | **DELETE** /api/v1/pivotview/{pivotViewId} | Delete a single pivot view
[**download_pivot_view_token_using_get**](PivotViewManagementApi.md#download_pivot_view_token_using_get) | **GET** /api/v1/pivotview/{pivotViewId}/token | This endpoint is deprecated. It not longer functions as intended, as pivotingquery results is now handled by cross tab queries. This endpoint will be removedon September 1, 2020.
[**download_pivot_view_using_get**](PivotViewManagementApi.md#download_pivot_view_using_get) | **GET** /api/v1/pivotview/{pivotViewId}/download | This endpoint is deprecated. It not longer functions as intended, as pivotingquery results is now handled by cross tab queries. This endpoint will be removedon September 1, 2020.
[**get_pivot_view_using_get**](PivotViewManagementApi.md#get_pivot_view_using_get) | **GET** /api/v1/pivotview/{pivotViewId} | Retrieve a single pivot view
[**list_pivot_views_using_get**](PivotViewManagementApi.md#list_pivot_views_using_get) | **GET** /api/v1/pivotview | Retrieve a list of pivot views
[**update_pivot_view_using_put**](PivotViewManagementApi.md#update_pivot_view_using_put) | **PUT** /api/v1/pivotview/{pivotViewId} | Update a single pivot view


# **create_pivot_view_using_post**
> BaseResponseOfPivotViewDto create_pivot_view_using_post(pivot_view_dto=pivot_view_dto)

Create a new pivot view

Creates a view from the provided information. Currently, persists the provided `additionalMetadata` field, which can store an arbitrary JSON definition of a pivot table view. This pivot table must be associated with a query, and can optionally be associated with a query result. When a query is deleted, its associated views are also deleted.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
pivot_view_dto = swagger_client.PivotViewDto() # PivotViewDto | The representation of the view to create (optional)

try:
    # Create a new pivot view
    api_response = api_instance.create_pivot_view_using_post(pivot_view_dto=pivot_view_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->create_pivot_view_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pivot_view_dto** | [**PivotViewDto**](PivotViewDto.md)| The representation of the view to create | [optional] 

### Return type

[**BaseResponseOfPivotViewDto**](BaseResponseOfPivotViewDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_pivot_view_using_delete**
> BaseResponseOfstring delete_pivot_view_using_delete(pivot_view_id)

Delete a single pivot view

Deletes a view that matches the provided ID.  This is an administrative method and should be assumed a hard-delete, given no capability to restore a deleted view is available.  A no-op if no such view exists.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
pivot_view_id = 'pivot_view_id_example' # str | The unique identifier of the pivot view

try:
    # Delete a single pivot view
    api_response = api_instance.delete_pivot_view_using_delete(pivot_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->delete_pivot_view_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pivot_view_id** | **str**| The unique identifier of the pivot view | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_pivot_view_token_using_get**
> BaseResponseOfTokenDto download_pivot_view_token_using_get(pivot_view_id)

This endpoint is deprecated. It not longer functions as intended, as pivotingquery results is now handled by cross tab queries. This endpoint will be removedon September 1, 2020.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
pivot_view_id = 'pivot_view_id_example' # str | The unique identifier of the pivot view

try:
    # This endpoint is deprecated. It not longer functions as intended, as pivotingquery results is now handled by cross tab queries. This endpoint will be removedon September 1, 2020.
    api_response = api_instance.download_pivot_view_token_using_get(pivot_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->download_pivot_view_token_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pivot_view_id** | **str**| The unique identifier of the pivot view | 

### Return type

[**BaseResponseOfTokenDto**](BaseResponseOfTokenDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_pivot_view_using_get**
> str download_pivot_view_using_get(pivot_view_id)

This endpoint is deprecated. It not longer functions as intended, as pivotingquery results is now handled by cross tab queries. This endpoint will be removedon September 1, 2020.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
pivot_view_id = 'pivot_view_id_example' # str | The unique identifier of the pivot view

try:
    # This endpoint is deprecated. It not longer functions as intended, as pivotingquery results is now handled by cross tab queries. This endpoint will be removedon September 1, 2020.
    api_response = api_instance.download_pivot_view_using_get(pivot_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->download_pivot_view_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pivot_view_id** | **str**| The unique identifier of the pivot view | 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pivot_view_using_get**
> BaseResponseOfPivotViewDto get_pivot_view_using_get(pivot_view_id)

Retrieve a single pivot view

Returns a view with the provided ID, or a 404 if no view matches the ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
pivot_view_id = 'pivot_view_id_example' # str | The unique identifier of the pivot view

try:
    # Retrieve a single pivot view
    api_response = api_instance.get_pivot_view_using_get(pivot_view_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->get_pivot_view_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pivot_view_id** | **str**| The unique identifier of the pivot view | 

### Return type

[**BaseResponseOfPivotViewDto**](BaseResponseOfPivotViewDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pivot_views_using_get**
> PagedResponseOfPivotViewDto list_pivot_views_using_get(query_id, limit=limit, cursor=cursor, offset=offset)

Retrieve a list of pivot views

Returns a paged list of views in the workspace of the request. If queryId is provided, the results are limited to only views associated with the query ID.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique query identifier to filter the views
limit = 56 # int | The number of views to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of pivot views
    api_response = api_instance.list_pivot_views_using_get(query_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->list_pivot_views_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique query identifier to filter the views | 
 **limit** | **int**| The number of views to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfPivotViewDto**](PagedResponseOfPivotViewDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_pivot_view_using_put**
> BaseResponseOfPivotViewDto update_pivot_view_using_put(pivot_view_id, pivot_view_dto=pivot_view_dto)

Update a single pivot view

Updates the view that matches the provided ID with the details provided in the body. The associated query can't be updated, so providing the query ID has no effect.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: oauth
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.PivotViewManagementApi(swagger_client.ApiClient(configuration))
pivot_view_id = 'pivot_view_id_example' # str | The unique identifier of the pivot view
pivot_view_dto = swagger_client.PivotViewDto() # PivotViewDto | The representation of the pivot view to create (optional)

try:
    # Update a single pivot view
    api_response = api_instance.update_pivot_view_using_put(pivot_view_id, pivot_view_dto=pivot_view_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PivotViewManagementApi->update_pivot_view_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pivot_view_id** | **str**| The unique identifier of the pivot view | 
 **pivot_view_dto** | [**PivotViewDto**](PivotViewDto.md)| The representation of the pivot view to create | [optional] 

### Return type

[**BaseResponseOfPivotViewDto**](BaseResponseOfPivotViewDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

