# swagger_client.TableManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_table_using_post**](TableManagementApi.md#create_table_using_post) | **POST** /api/v1/table | Create a new table
[**delete_table_using_delete**](TableManagementApi.md#delete_table_using_delete) | **DELETE** /api/v1/table/{tableId} | Delete a single table
[**get_dependents_using_get**](TableManagementApi.md#get_dependents_using_get) | **GET** /api/v1/table/{tableId}/dependents | Retrieve a list of dependents
[**get_import_info_using_get**](TableManagementApi.md#get_import_info_using_get) | **GET** /api/v1/table/{tableId}/importInfo | Retrieve import information
[**get_table_using_get**](TableManagementApi.md#get_table_using_get) | **GET** /api/v1/table/{tableId} | Retrieve a single table
[**get_tables_using_get**](TableManagementApi.md#get_tables_using_get) | **GET** /api/v1/table | Retrieve a list of tables
[**import_file_using_post**](TableManagementApi.md#import_file_using_post) | **POST** /api/v1/table/{tableId}/import | Import a single file
[**import_from_spreadsheets_using_post**](TableManagementApi.md#import_from_spreadsheets_using_post) | **POST** /api/v1/table/{tableId}/spreadsheet/import | Import from spreadsheets
[**unimport_file_using_delete**](TableManagementApi.md#unimport_file_using_delete) | **DELETE** /api/v1/table/{tableId}/import/{fileId} | Unimport a single file
[**update_table_using_put**](TableManagementApi.md#update_table_using_put) | **PUT** /api/v1/table/{tableId} | Update a single table


# **create_table_using_post**
> BaseResponseOfTableDto create_table_using_post(body=body)

Create a new table

Creates a table in the database with the specified schema. For type, specify either a dimension or data table. In the interface, data tables appear as fact tables.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
body = swagger_client.TableDto() # TableDto | The representation of the table to create (optional)

try:
    # Create a new table
    api_response = api_instance.create_table_using_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->create_table_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TableDto**](TableDto.md)| The representation of the table to create | [optional] 

### Return type

[**BaseResponseOfTableDto**](BaseResponseOfTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_table_using_delete**
> BaseResponseOfstring delete_table_using_delete(table_id)

Delete a single table

Soft-deletes the table with the provided ID.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table

try:
    # Delete a single table
    api_response = api_instance.delete_table_using_delete(table_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->delete_table_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependents_using_get**
> PagedResponseOfQueryDto get_dependents_using_get(table_id, limit=limit, cursor=cursor, offset=offset)

Retrieve a list of dependents

Returns a list of all queries that use the table with provided ID as a datasource. If a shared table, this may include queries outside of the current OAuth context.  Permission is checked only for the table ID provided, _not_ on the returned list of queries.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table
limit = 56 # int | The number of folders to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of dependents
    api_response = api_instance.get_dependents_using_get(table_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->get_dependents_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 
 **limit** | **int**| The number of folders to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfQueryDto**](PagedResponseOfQueryDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_import_info_using_get**
> BaseResponseOfImportInfoDto get_import_info_using_get(table_id)

Retrieve import information

Returns information around imported files for a table.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table

try:
    # Retrieve import information
    api_response = api_instance.get_import_info_using_get(table_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->get_import_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 

### Return type

[**BaseResponseOfImportInfoDto**](BaseResponseOfImportInfoDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_table_using_get**
> BaseResponseOfTableDto get_table_using_get(table_id)

Retrieve a single table

Returns a table with the provided ID, or a 404 if no such table is found.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table

try:
    # Retrieve a single table
    api_response = api_instance.get_table_using_get(table_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->get_table_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 

### Return type

[**BaseResponseOfTableDto**](BaseResponseOfTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables_using_get**
> PagedResponseOfTableDto get_tables_using_get(include_shared=include_shared, limit=limit, cursor=cursor, offset=offset)

Retrieve a list of tables

Returns all tables available in the workspace.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
include_shared = false # bool | If true, returns all tables shared with the workspace associated with the request. If false, returns only tables the workspace owns. (optional) (default to false)
limit = 56 # int | the number of folders to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | a paging cursor; if included the limit is ignored (optional)
offset = 789 # int | The item to start with on the page, must be greater than or equal to 0, will default to 0 (optional)

try:
    # Retrieve a list of tables
    api_response = api_instance.get_tables_using_get(include_shared=include_shared, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->get_tables_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_shared** | **bool**| If true, returns all tables shared with the workspace associated with the request. If false, returns only tables the workspace owns. | [optional] [default to false]
 **limit** | **int**| the number of folders to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| a paging cursor; if included the limit is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, must be greater than or equal to 0, will default to 0 | [optional] 

### Return type

[**PagedResponseOfTableDto**](PagedResponseOfTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_file_using_post**
> BaseResponseOfFileMetaDto import_file_using_post(table_id, import_dto=import_dto)

Import a single file

Imports the provided file into the associated table, and immediately returns a file meta object with an ID that can be used to poll the file controller for status.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table
import_dto = swagger_client.ImportDto() # ImportDto | The representation of the table to import (optional)

try:
    # Import a single file
    api_response = api_instance.import_file_using_post(table_id, import_dto=import_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->import_file_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 
 **import_dto** | [**ImportDto**](ImportDto.md)| The representation of the table to import | [optional] 

### Return type

[**BaseResponseOfFileMetaDto**](BaseResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **import_from_spreadsheets_using_post**
> BaseResponseOfFileMetaDto import_from_spreadsheets_using_post(table_id, import_from_spreadsheet_dto=import_from_spreadsheet_dto)

Import from spreadsheets

Imports spreadsheet data and immediately returns a file meta result. This DTO has an ID, which can be used to poll on status via the file controller.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table
import_from_spreadsheet_dto = swagger_client.ImportFromSpreadsheetDto() # ImportFromSpreadsheetDto | The representation of the table to update (optional)

try:
    # Import from spreadsheets
    api_response = api_instance.import_from_spreadsheets_using_post(table_id, import_from_spreadsheet_dto=import_from_spreadsheet_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->import_from_spreadsheets_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 
 **import_from_spreadsheet_dto** | [**ImportFromSpreadsheetDto**](ImportFromSpreadsheetDto.md)| The representation of the table to update | [optional] 

### Return type

[**BaseResponseOfFileMetaDto**](BaseResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unimport_file_using_delete**
> BaseResponseOfFileMetaDto unimport_file_using_delete(table_id, file_id, force=force)

Unimport a single file

Unimports the provided file from the provided table. Returns a 409 if the file is not in an imported state, or a 404 if the file can't be found.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table
file_id = 'file_id_example' # str | The unique identifier of the file
force = 'false' # str | If true, unimports and deletes file from the table (optional) (default to false)

try:
    # Unimport a single file
    api_response = api_instance.unimport_file_using_delete(table_id, file_id, force=force)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->unimport_file_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 
 **file_id** | **str**| The unique identifier of the file | 
 **force** | **str**| If true, unimports and deletes file from the table | [optional] [default to false]

### Return type

[**BaseResponseOfFileMetaDto**](BaseResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_table_using_put**
> BaseResponseOfTableDto update_table_using_put(table_id, table_dto=table_dto)

Update a single table

Updates an existing table with the provided information. Include all user-defined table columns with the request. For type, specify either a dimension or data table. In the interface, data tables appear as fact tables.  * If the table has no imported data, user-defined columns not included with the request are deleted, and columns are sorted according to their order in the request.  * If the table has imported data, any columns with names not already in the table are considered new. This equality check is case-insensitive. Any new columns appear after other user-defined columns, but before any meta columns, which start with `_`.

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
api_instance = swagger_client.TableManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique identifier of the table
table_dto = swagger_client.TableDto() # TableDto | The representation of the table to update (optional)

try:
    # Update a single table
    api_response = api_instance.update_table_using_put(table_id, table_dto=table_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TableManagementApi->update_table_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique identifier of the table | 
 **table_dto** | [**TableDto**](TableDto.md)| The representation of the table to update | [optional] 

### Return type

[**BaseResponseOfTableDto**](BaseResponseOfTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

