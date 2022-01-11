# swagger_client.AdministrativeTasksApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_workspace_using_delete**](AdministrativeTasksApi.md#delete_workspace_using_delete) | **DELETE** /api/v1/admin/account | Delete a single workspace
[**export_workspace_using_get**](AdministrativeTasksApi.md#export_workspace_using_get) | **GET** /api/v1/admin/export | Export a single workspace
[**find_workspace_files_by_size_using_get**](AdministrativeTasksApi.md#find_workspace_files_by_size_using_get) | **GET** /api/v1/admin/usage/filesBySize | Retrieve workspace files by size
[**get_workspace_query_usage_using_get**](AdministrativeTasksApi.md#get_workspace_query_usage_using_get) | **GET** /api/v1/admin/usage/query | Retrieve workspace query usage
[**get_workspace_upload_usage_using_get**](AdministrativeTasksApi.md#get_workspace_upload_usage_using_get) | **GET** /api/v1/admin/usage/upload | Retrieve workspace upload usage
[**import_data_using_post**](AdministrativeTasksApi.md#import_data_using_post) | **POST** /api/v1/admin/import | Import data
[**validate_files_using_post**](AdministrativeTasksApi.md#validate_files_using_post) | **POST** /api/v1/admin/validation/files | Validate files
[**validate_tables_using_post**](AdministrativeTasksApi.md#validate_tables_using_post) | **POST** /api/v1/admin/validation/tables | Validate tables


# **delete_workspace_using_delete**
> BaseResponseOfstring delete_workspace_using_delete()

Delete a single workspace

Deletes all information in the workspace of the request. <b>This is a final operation and can't be undone</b>. Any state left in the workspace due to an error is in an indeterminate state and shouldn't be trusted. Some non-private information may be kept for auditing and metric purposes.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))

try:
    # Delete a single workspace
    api_response = api_instance.delete_workspace_using_delete()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->delete_workspace_using_delete: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_workspace_using_get**
> BaseResponseOfTokenDto export_workspace_using_get()

Export a single workspace

Returns a file that represents the entirety of the workspace of the request. You can upload this file into another workspace to replicate this one.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))

try:
    # Export a single workspace
    api_response = api_instance.export_workspace_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->export_workspace_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BaseResponseOfTokenDto**](BaseResponseOfTokenDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_workspace_files_by_size_using_get**
> PagedResponseOfFileMetaDto find_workspace_files_by_size_using_get(limit=limit, cursor=cursor, offset=offset)

Retrieve workspace files by size

Returns a paged collection of the file meta associated with the workspace of the request, ordered by size.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of file meta objects to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve workspace files by size
    api_response = api_instance.find_workspace_files_by_size_using_get(limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->find_workspace_files_by_size_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of file meta objects to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfFileMetaDto**](PagedResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_query_usage_using_get**
> BaseResponseOflong get_workspace_query_usage_using_get(start_date=start_date, stop_date=stop_date)

Retrieve workspace query usage

Returns a Long that represents the number of bytes queried by the workspace of the request since the start time provided.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))
start_date = '1970-01-01' # str | The earliest date of usage to consider (optional) (default to 1970-01-01)
stop_date = '9999-01-01' # str | The end date of usage to consider (optional) (default to 9999-01-01)

try:
    # Retrieve workspace query usage
    api_response = api_instance.get_workspace_query_usage_using_get(start_date=start_date, stop_date=stop_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->get_workspace_query_usage_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| The earliest date of usage to consider | [optional] [default to 1970-01-01]
 **stop_date** | **str**| The end date of usage to consider | [optional] [default to 9999-01-01]

### Return type

[**BaseResponseOflong**](BaseResponseOflong.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_workspace_upload_usage_using_get**
> BaseResponseOflong get_workspace_upload_usage_using_get(start_date=start_date, stop_date=stop_date)

Retrieve workspace upload usage

Returns a Long that represents the number of bytes uploaded by the workspace associated with this request from the start time provided to now.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))
start_date = '1970-01-01' # str | The starting point to begin considering usage (optional) (default to 1970-01-01)
stop_date = '9999-01-01' # str | The ending point when considering usage (optional) (default to 9999-01-01)

try:
    # Retrieve workspace upload usage
    api_response = api_instance.get_workspace_upload_usage_using_get(start_date=start_date, stop_date=stop_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->get_workspace_upload_usage_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **str**| The starting point to begin considering usage | [optional] [default to 1970-01-01]
 **stop_date** | **str**| The ending point when considering usage | [optional] [default to 9999-01-01]

### Return type

[**BaseResponseOflong**](BaseResponseOflong.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_data_using_post**
> BaseResponseOfstring import_data_using_post(file=file, wipe=wipe)

Import data

By default, deletes all information in the workspace of the request. <b>This is a final operation and can't be undone.</b>  Any state left in the workspace due to an error is in an indeterminate state and shouldn't be trusted. Some non-private information may be kept for auditing and metric purposes. After the delete, it then imports the tables, tags, and queries in the provided cb file into the workspace. <br><br>This is an asynchronous operation. Returns a 201 when the file is correctly decoded and its tables, queries, and tags are saved. Files continue to import after this call completes.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))
file = '/path/to/file.txt' # file | The file containing workspace information to import (optional)
wipe = true # bool | wipe (optional) (default to true)

try:
    # Import data
    api_response = api_instance.import_data_using_post(file=file, wipe=wipe)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->import_data_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| The file containing workspace information to import | [optional] 
 **wipe** | **bool**| wipe | [optional] [default to true]

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_files_using_post**
> BaseResponseOfValidateFilesDto validate_files_using_post(validate_files_dto=validate_files_dto)

Validate files

Validates files associated with the provided table ID. Validation repairs any files in an inconsistent state, and deletes those without enough state to recover. All files deleted or repaired are returned.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))
validate_files_dto = swagger_client.StartValidateFilesDto() # StartValidateFilesDto | The representation of the file to validate (optional)

try:
    # Validate files
    api_response = api_instance.validate_files_using_post(validate_files_dto=validate_files_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->validate_files_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **validate_files_dto** | [**StartValidateFilesDto**](StartValidateFilesDto.md)| The representation of the file to validate | [optional] 

### Return type

[**BaseResponseOfValidateFilesDto**](BaseResponseOfValidateFilesDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_tables_using_post**
> BaseResponseOfValidateTablesDto validate_tables_using_post()

Validate tables

Validates the tables in the workspace associated with the request. Validation returns an entity that indicates the tables deleted due to bad state, and those with enough state and repaired.

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
api_instance = swagger_client.AdministrativeTasksApi(swagger_client.ApiClient(configuration))

try:
    # Validate tables
    api_response = api_instance.validate_tables_using_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdministrativeTasksApi->validate_tables_using_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BaseResponseOfValidateTablesDto**](BaseResponseOfValidateTablesDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

