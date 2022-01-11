# swagger_client.FileManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_file_using_delete**](FileManagementApi.md#delete_file_using_delete) | **DELETE** /api/v1/file/{fileId} | Delete a single file
[**download_file_using_get**](FileManagementApi.md#download_file_using_get) | **GET** /api/v1/file/{fileId}/download | Download a single file
[**export_file_to_spreadsheets_using_post**](FileManagementApi.md#export_file_to_spreadsheets_using_post) | **POST** /api/v1/file/{fileId}/export | Export a file to spreadsheets
[**get_errors_using_get**](FileManagementApi.md#get_errors_using_get) | **GET** /api/v1/file/{fileId}/error | Retrieve errors
[**get_file_using_get**](FileManagementApi.md#get_file_using_get) | **GET** /api/v1/file/{fileId} | Retrieve a single file
[**get_files_using_get**](FileManagementApi.md#get_files_using_get) | **GET** /api/v1/file | Retrieve a list of files
[**upload_file_using_post**](FileManagementApi.md#upload_file_using_post) | **POST** /api/v1/file | Upload a single file
[**validate_filename_using_get**](FileManagementApi.md#validate_filename_using_get) | **GET** /api/v1/file/validateName | Validate whether a file with the filename can be uploaded to the table


# **delete_file_using_delete**
> BaseResponseOfstring delete_file_using_delete(file_id)

Delete a single file

Unstages the file with the provided ID. The file must have a STAGED status; if the file isn't STAGED, returns a 409 status. If the file isn't found, this is a no-op.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The unique identifier of the file

try:
    # Delete a single file
    api_response = api_instance.delete_file_using_delete(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->delete_file_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_using_get**
> str download_file_using_get(file_id)

Download a single file

Returns a file with the provided ID, which points to a file meta ID.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The unique identifier of the file

try:
    # Download a single file
    api_response = api_instance.download_file_using_get(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->download_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_file_to_spreadsheets_using_post**
> BaseResponseOfSpreadsheetInfoDto export_file_to_spreadsheets_using_post(file_id, export_file_dto=export_file_dto)

Export a file to spreadsheets

Exports the file ID identified in the path to the spreadsheet identified by the provided URL. If the URL string is empty, creates and returns a new spreadsheet and its sheet IDs.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The unique identifier of the file
export_file_dto = swagger_client.ExportFileDto() # ExportFileDto | The representation of the file to export (optional)

try:
    # Export a file to spreadsheets
    api_response = api_instance.export_file_to_spreadsheets_using_post(file_id, export_file_dto=export_file_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->export_file_to_spreadsheets_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 
 **export_file_dto** | [**ExportFileDto**](ExportFileDto.md)| The representation of the file to export | [optional] 

### Return type

[**BaseResponseOfSpreadsheetInfoDto**](BaseResponseOfSpreadsheetInfoDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_errors_using_get**
> PagedResponseOfImportErrorDto get_errors_using_get(file_id, limit=limit, cursor=cursor, offset=offset)

Retrieve errors

Returns a paged list of operation errors during the upload, import, or tagging processes for the provided file ID, if they exist. This list is immutable and may be empty if no errors have occurred. If errors exist we recommend fixing them and reimporting your file

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The unique identifier of the file
limit = 56 # int | The number of errors to return, from 1 to 50; by default, 50 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve errors
    api_response = api_instance.get_errors_using_get(file_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->get_errors_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 
 **limit** | **int**| The number of errors to return, from 1 to 50; by default, 50 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfImportErrorDto**](PagedResponseOfImportErrorDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_file_using_get**
> BaseResponseOfFileMetaDto get_file_using_get(file_id)

Retrieve a single file

Returns the file meta that matches the provided ID, or a 404 if an associated file can't be found.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
file_id = 'file_id_example' # str | The unique identifier of the file

try:
    # Retrieve a single file
    api_response = api_instance.get_file_using_get(file_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->get_file_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **str**| The unique identifier of the file | 

### Return type

[**BaseResponseOfFileMetaDto**](BaseResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files_using_get**
> PagedResponseOfFileMetaDto get_files_using_get(table_id, limit=limit, cursor=cursor, offset=offset, sort_order=sort_order, sort_by=sort_by, search_text=search_text)

Retrieve a list of files

Returns a paged list of all files associated with the provided table ID, as well as metadata associated with each file.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique table identifier associated with this file
limit = 56 # int | The number of files to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)
sort_order = 'sort_order_example' # str | The sort order for the files being returned (optional)
sort_by = 'sort_by_example' # str | The column to use the sort order on (optional)
search_text = 'search_text_example' # str | The text to filter the results upon; matching the file name (optional)

try:
    # Retrieve a list of files
    api_response = api_instance.get_files_using_get(table_id, limit=limit, cursor=cursor, offset=offset, sort_order=sort_order, sort_by=sort_by, search_text=search_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->get_files_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique table identifier associated with this file | 
 **limit** | **int**| The number of files to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 
 **sort_order** | **str**| The sort order for the files being returned | [optional] 
 **sort_by** | **str**| The column to use the sort order on | [optional] 
 **search_text** | **str**| The text to filter the results upon; matching the file name | [optional] 

### Return type

[**PagedResponseOfFileMetaDto**](PagedResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_file_using_post**
> BaseResponseOfFileMetaDto upload_file_using_post(table_id, file=file, name=name, url=url, source=source, delimiter=delimiter)

Upload a single file

Accepts CSV, TSV, or JSON files, or a ZIP file that contains a single CSV, TSV, or JSON file. If a ZIP, it must contain a CSV, TSV, or JSON file, and the name of the CSV, TSV, or JSON file is also used with the imported file. Downloading this file again downloads the source. <br><br> You can also upload a URL to the file, such as an S3-signed URL to a file in an S3 bucket. The endpoint then makes a request to get the file using a simple unauthenticated `GET` request. <br><br> Note that all files uploaded must have a .csv, .tsv, or .json extension. JSON files are expected to have a single JSON record per line; a JSON file is a series of JSON objects delimited by a newline character.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The unique table identifier associated with this file
file = '/path/to/file.txt' # file | The physical file to upload (optional)
name = 'name_example' # str | No longer in use, here to ensure backwards compatibility (optional)
url = 'url_example' # str | No longer in use, here to ensure backwards compatibility (optional)
source = 'source_example' # str | The data source to associate with the file, no more than 255 characters. This field is not in use; it only keeps track of the source (optional)
delimiter = 'delimiter_example' # str | The character to use as a delimiter within the file to separate one field from another.  The default is comma (optional)

try:
    # Upload a single file
    api_response = api_instance.upload_file_using_post(table_id, file=file, name=name, url=url, source=source, delimiter=delimiter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->upload_file_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The unique table identifier associated with this file | 
 **file** | **file**| The physical file to upload | [optional] 
 **name** | **str**| No longer in use, here to ensure backwards compatibility | [optional] 
 **url** | **str**| No longer in use, here to ensure backwards compatibility | [optional] 
 **source** | **str**| The data source to associate with the file, no more than 255 characters. This field is not in use; it only keeps track of the source | [optional] 
 **delimiter** | **str**| The character to use as a delimiter within the file to separate one field from another.  The default is comma | [optional] 

### Return type

[**BaseResponseOfFileMetaDto**](BaseResponseOfFileMetaDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_filename_using_get**
> BaseResponseOfstring validate_filename_using_get(table_id, filename)

Validate whether a file with the filename can be uploaded to the table

If the filename is valid, this returns 200. If the table already has a file with the same name, this returns 409. If the user isn't allowed to read the table, or if the table isn't found, this returns 404.

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
api_instance = swagger_client.FileManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The ID of the table to upload the file to
filename = 'filename_example' # str | The name of the file to upload

try:
    # Validate whether a file with the filename can be uploaded to the table
    api_response = api_instance.validate_filename_using_get(table_id, filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FileManagementApi->validate_filename_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The ID of the table to upload the file to | 
 **filename** | **str**| The name of the file to upload | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

