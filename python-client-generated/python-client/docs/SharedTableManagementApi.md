# swagger_client.SharedTableManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_shared_table_using_post**](SharedTableManagementApi.md#create_shared_table_using_post) | **POST** /api/v1/sharedtable | Create a new shared table
[**delete_shared_table_using_delete**](SharedTableManagementApi.md#delete_shared_table_using_delete) | **DELETE** /api/v1/sharedtable/{sharedTableId} | Delete a single shared table
[**get_shared_table_using_get**](SharedTableManagementApi.md#get_shared_table_using_get) | **GET** /api/v1/sharedtable/{sharedTableId} | Retrieve a single shared table
[**list_shared_tables_using_get**](SharedTableManagementApi.md#list_shared_tables_using_get) | **GET** /api/v1/sharedtable | Retrieve a list of shared tables


# **create_shared_table_using_post**
> BaseResponseOfSharedTableDto create_shared_table_using_post(shared_table_dto=shared_table_dto)

Create a new shared table

Creates a shared table instance between the workspace of the request and the workspace provided in the body.

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
api_instance = swagger_client.SharedTableManagementApi(swagger_client.ApiClient(configuration))
shared_table_dto = swagger_client.SharedTableDto() # SharedTableDto | The representation of the shared table to create (optional)

try:
    # Create a new shared table
    api_response = api_instance.create_shared_table_using_post(shared_table_dto=shared_table_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedTableManagementApi->create_shared_table_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_table_dto** | [**SharedTableDto**](SharedTableDto.md)| The representation of the shared table to create | [optional] 

### Return type

[**BaseResponseOfSharedTableDto**](BaseResponseOfSharedTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_shared_table_using_delete**
> BaseResponseOfstring delete_shared_table_using_delete(shared_table_id)

Delete a single shared table

Deletes the linkages between the source and destination of a shared table that matches the provided ID; the actual table itself is left intact. If no such shared table exists, this is a no-op.

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
api_instance = swagger_client.SharedTableManagementApi(swagger_client.ApiClient(configuration))
shared_table_id = 'shared_table_id_example' # str | The unique identifier of the shared table

try:
    # Delete a single shared table
    api_response = api_instance.delete_shared_table_using_delete(shared_table_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedTableManagementApi->delete_shared_table_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_table_id** | **str**| The unique identifier of the shared table | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_table_using_get**
> BaseResponseOfSharedTableDto get_shared_table_using_get(shared_table_id, shared_with_me=shared_with_me)

Retrieve a single shared table

Returns a shared table that matches the provided ID, or a 404 if no matching shared table is found.

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
api_instance = swagger_client.SharedTableManagementApi(swagger_client.ApiClient(configuration))
shared_table_id = 'shared_table_id_example' # str | The unique identifier of the shared table
shared_with_me = true # bool | If true, returns a shared table with the provided ID that has been shared _to_—rather than from—the workspace of the request. (optional)

try:
    # Retrieve a single shared table
    api_response = api_instance.get_shared_table_using_get(shared_table_id, shared_with_me=shared_with_me)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedTableManagementApi->get_shared_table_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shared_table_id** | **str**| The unique identifier of the shared table | 
 **shared_with_me** | **bool**| If true, returns a shared table with the provided ID that has been shared _to_—rather than from—the workspace of the request. | [optional] 

### Return type

[**BaseResponseOfSharedTableDto**](BaseResponseOfSharedTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shared_tables_using_get**
> PagedResponseOfSharedTableDto list_shared_tables_using_get(table_id=table_id, shared_with_me=shared_with_me, limit=limit, cursor=cursor, offset=offset)

Retrieve a list of shared tables

Returns a list of shared tables associated with the workspace of the request.

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
api_instance = swagger_client.SharedTableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique table identifier associated with the shared table (optional)
shared_with_me = true # bool | If true, returns a list of tables that have been shared _to_ it rather than from it. The entities contain both the shared table entity _and_ the table being shared. If true, `tableId` is ignored. (optional)
limit = 56 # int | The number of shared files to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of shared tables
    api_response = api_instance.list_shared_tables_using_get(table_id=table_id, shared_with_me=shared_with_me, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SharedTableManagementApi->list_shared_tables_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique table identifier associated with the shared table | [optional] 
 **shared_with_me** | **bool**| If true, returns a list of tables that have been shared _to_ it rather than from it. The entities contain both the shared table entity _and_ the table being shared. If true, &#x60;tableId&#x60; is ignored. | [optional] 
 **limit** | **int**| The number of shared files to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfSharedTableDto**](PagedResponseOfSharedTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

