# swagger_client.ConnectionManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connection_using_get**](ConnectionManagementApi.md#get_connection_using_get) | **GET** /api/v1/connections/{connectionId} | Get connection details
[**get_refresh_batch_status_using_get**](ConnectionManagementApi.md#get_refresh_batch_status_using_get) | **GET** /api/v1/connections/batch/refresh/{batchId} | Gets the status of a batch refresh
[**get_refresh_status_using_get**](ConnectionManagementApi.md#get_refresh_status_using_get) | **GET** /api/v1/connections/{connectionId}/status | Get connection refresh status
[**list_connections_using_get**](ConnectionManagementApi.md#list_connections_using_get) | **GET** /api/v1/connections | List connections
[**refresh_batch_using_post**](ConnectionManagementApi.md#refresh_batch_using_post) | **POST** /api/v1/connections/batch/refresh | Refresh batch of connections
[**refresh_connection_using_post**](ConnectionManagementApi.md#refresh_connection_using_post) | **POST** /api/v1/connections/{connectionId}/refresh | Refresh connection


# **get_connection_using_get**
> BaseResponseOfConnectionDto get_connection_using_get(connection_id)

Get connection details

Returns details about a specific connection, based on its ID

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
api_instance = swagger_client.ConnectionManagementApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | The ID of the connection to return details about

try:
    # Get connection details
    api_response = api_instance.get_connection_using_get(connection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionManagementApi->get_connection_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the connection to return details about | 

### Return type

[**BaseResponseOfConnectionDto**](BaseResponseOfConnectionDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_batch_status_using_get**
> BaseResponseOfRefreshBatchDto get_refresh_batch_status_using_get(batch_id)

Gets the status of a batch refresh

Returns details about a specific batch refresh, based on its ID.

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
api_instance = swagger_client.ConnectionManagementApi(swagger_client.ApiClient(configuration))
batch_id = 'batch_id_example' # str | The ID of the batch to return details about

try:
    # Gets the status of a batch refresh
    api_response = api_instance.get_refresh_batch_status_using_get(batch_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionManagementApi->get_refresh_batch_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **batch_id** | **str**| The ID of the batch to return details about | 

### Return type

[**BaseResponseOfRefreshBatchDto**](BaseResponseOfRefreshBatchDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_refresh_status_using_get**
> BaseResponseOfConnectionRunDto get_refresh_status_using_get(connection_id, job_id=job_id)

Get connection refresh status

Returns details about a specific connection refresh status, based on its ID. To retrieve details about a specific refresh, provide its 'jobId'.

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
api_instance = swagger_client.ConnectionManagementApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | The ID of the connection to return details about
job_id = 'job_id_example' # str | The ID of the job running for a connection (optional)

try:
    # Get connection refresh status
    api_response = api_instance.get_refresh_status_using_get(connection_id, job_id=job_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionManagementApi->get_refresh_status_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the connection to return details about | 
 **job_id** | **str**| The ID of the job running for a connection | [optional] 

### Return type

[**BaseResponseOfConnectionRunDto**](BaseResponseOfConnectionRunDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connections_using_get**
> PagedResponseOfConnectionDto list_connections_using_get(source_type=source_type, destination_type=destination_type, source_id=source_id, destination_id=destination_id, limit=limit, cursor=cursor, offset=offset)

List connections

A pageable endpoint to list data connections between features of the Workiva platform

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
api_instance = swagger_client.ConnectionManagementApi(swagger_client.ApiClient(configuration))
source_type = 'source_type_example' # str | The type of file or item the connection pulls data from (optional)
destination_type = 'destination_type_example' # str | The type of file or item the connection sends data to (optional)
source_id = 'source_id_example' # str | The ID of the file or item the connection pulls data from (optional)
destination_id = 'destination_id_example' # str | The ID of the file or item the connection sends data to (optional)
limit = 56 # int | The number of connections to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # List connections
    api_response = api_instance.list_connections_using_get(source_type=source_type, destination_type=destination_type, source_id=source_id, destination_id=destination_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionManagementApi->list_connections_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **source_type** | **str**| The type of file or item the connection pulls data from | [optional] 
 **destination_type** | **str**| The type of file or item the connection sends data to | [optional] 
 **source_id** | **str**| The ID of the file or item the connection pulls data from | [optional] 
 **destination_id** | **str**| The ID of the file or item the connection sends data to | [optional] 
 **limit** | **int**| The number of connections to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfConnectionDto**](PagedResponseOfConnectionDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_batch_using_post**
> BaseResponseOfRefreshBatchDto refresh_batch_using_post(refresh_connection_dtos)

Refresh batch of connections

Refreshes multiple connections at once, based on their IDs

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
api_instance = swagger_client.ConnectionManagementApi(swagger_client.ApiClient(configuration))
refresh_connection_dtos = [swagger_client.RefreshConnectionDto()] # list[RefreshConnectionDto] | refreshConnectionDtos

try:
    # Refresh batch of connections
    api_response = api_instance.refresh_batch_using_post(refresh_connection_dtos)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionManagementApi->refresh_batch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh_connection_dtos** | [**list[RefreshConnectionDto]**](RefreshConnectionDto.md)| refreshConnectionDtos | 

### Return type

[**BaseResponseOfRefreshBatchDto**](BaseResponseOfRefreshBatchDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_connection_using_post**
> BaseResponseOfConnectionRunDto refresh_connection_using_post(connection_id, refresh_connection_dto)

Refresh connection

Refreshes a specific connection, based on its ID

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
api_instance = swagger_client.ConnectionManagementApi(swagger_client.ApiClient(configuration))
connection_id = 'connection_id_example' # str | The ID of the connection to refresh
refresh_connection_dto = swagger_client.RefreshConnectionDto() # RefreshConnectionDto | refreshConnectionDto

try:
    # Refresh connection
    api_response = api_instance.refresh_connection_using_post(connection_id, refresh_connection_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionManagementApi->refresh_connection_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_id** | **str**| The ID of the connection to refresh | 
 **refresh_connection_dto** | [**RefreshConnectionDto**](RefreshConnectionDto.md)| refreshConnectionDto | 

### Return type

[**BaseResponseOfConnectionRunDto**](BaseResponseOfConnectionRunDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

