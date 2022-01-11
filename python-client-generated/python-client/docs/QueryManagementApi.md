# swagger_client.QueryManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_query_using_delete**](QueryManagementApi.md#cancel_query_using_delete) | **DELETE** /api/v1/queryresult/{queryResultId} | Cancel a running query
[**create_query_using_post**](QueryManagementApi.md#create_query_using_post) | **POST** /api/v1/query | Create a new query
[**delete_query_using_delete**](QueryManagementApi.md#delete_query_using_delete) | **DELETE** /api/v1/query/{queryId} | Delete a single query
[**download_query_result_using_get**](QueryManagementApi.md#download_query_result_using_get) | **GET** /api/v1/queryresult/{queryResultId}/download | Download a query result
[**export_query_result_to_spreadsheets_using_post**](QueryManagementApi.md#export_query_result_to_spreadsheets_using_post) | **POST** /api/v1/queryresult/{queryResultId}/export | Export query result to spreadsheets
[**get_dependencies_using_get**](QueryManagementApi.md#get_dependencies_using_get) | **GET** /api/v1/query/{queryId}/dependencies | Retrieve dependencies
[**get_query_column_data_using_post**](QueryManagementApi.md#get_query_column_data_using_post) | **POST** /api/v1/query/data | Retrieve query column data
[**get_query_result_using_get**](QueryManagementApi.md#get_query_result_using_get) | **GET** /api/v1/queryresult/{queryResultId} | Retrieve a single query result
[**get_query_using_get**](QueryManagementApi.md#get_query_using_get) | **GET** /api/v1/query/{queryId} | Retrieve a single query
[**get_tables_dependent_on_query_using_get**](QueryManagementApi.md#get_tables_dependent_on_query_using_get) | **GET** /api/v1/query/{queryId}/dependents | Retrieve a list of dependents
[**is_query_valid_using_post**](QueryManagementApi.md#is_query_valid_using_post) | **POST** /api/v1/query/validation | Parses the query to determine if it is valid
[**list_queries_using_get**](QueryManagementApi.md#list_queries_using_get) | **GET** /api/v1/query | Retrieve list of queries
[**list_query_results_using_get**](QueryManagementApi.md#list_query_results_using_get) | **GET** /api/v1/queryresult | Retrieve a list of query results
[**preview_query_using_post**](QueryManagementApi.md#preview_query_using_post) | **POST** /api/v1/query/preview/{tableId} | Preview a query
[**run_query_using_post**](QueryManagementApi.md#run_query_using_post) | **POST** /api/v1/queryresult | Execute a query
[**update_query_using_put**](QueryManagementApi.md#update_query_using_put) | **PUT** /api/v1/query/{queryId} | Update a single query


# **cancel_query_using_delete**
> BaseResponseOfQueryResultDto cancel_query_using_delete(query_result_id)

Cancel a running query

Cancels a running query based on the provided result ID, and returns a cancelled result unless the query's already in a COMPLETED state.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_result_id = 'query_result_id_example' # str | The unique identifier of the query result

try:
    # Cancel a running query
    api_response = api_instance.cancel_query_using_delete(query_result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->cancel_query_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_result_id** | **str**| The unique identifier of the query result | 

### Return type

[**BaseResponseOfQueryResultDto**](BaseResponseOfQueryResultDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_query_using_post**
> BaseResponseOfQueryDto create_query_using_post(query_dto=query_dto)

Create a new query

Creates a query object and validates full permissions to ensure the requestor has access to all data sources being queried. This endpoint _doesn't_ execute the query; to execute, call the POST /queryresult method.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_dto = swagger_client.QueryDto() # QueryDto | The representation of the query to create (optional)

try:
    # Create a new query
    api_response = api_instance.create_query_using_post(query_dto=query_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->create_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_dto** | [**QueryDto**](QueryDto.md)| The representation of the query to create | [optional] 

### Return type

[**BaseResponseOfQueryDto**](BaseResponseOfQueryDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_query_using_delete**
> BaseResponseOfstring delete_query_using_delete(query_id)

Delete a single query

Deletes the query that matches the provided ID. If no such query is found, this is a no-op.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique identifier of the query

try:
    # Delete a single query
    api_response = api_instance.delete_query_using_delete(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->delete_query_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique identifier of the query | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_query_result_using_get**
> str download_query_result_using_get(query_result_id)

Download a query result

Uses the Token Management API to create a token with the query result ID, which it then uses to download a CSV file of the query results.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_result_id = 'query_result_id_example' # str | The unique identifier of the query result

try:
    # Download a query result
    api_response = api_instance.download_query_result_using_get(query_result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->download_query_result_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_result_id** | **str**| The unique identifier of the query result | 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_query_result_to_spreadsheets_using_post**
> BaseResponseOfstring export_query_result_to_spreadsheets_using_post(query_result_id, dto=dto)

Export query result to spreadsheets

Exports a query result with the provided ID to Spreadsheets. To determine where to export the results, the request body should include a URL copied and pasted from the Spreadsheets UI. Returns a 404 if no matching query result is found.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_result_id = 'query_result_id_example' # str | The unique identifier of the query result
dto = swagger_client.ExportQueryResultDto() # ExportQueryResultDto | The representation of the export query result (optional)

try:
    # Export query result to spreadsheets
    api_response = api_instance.export_query_result_to_spreadsheets_using_post(query_result_id, dto=dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->export_query_result_to_spreadsheets_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_result_id** | **str**| The unique identifier of the query result | 
 **dto** | [**ExportQueryResultDto**](ExportQueryResultDto.md)| The representation of the export query result | [optional] 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dependencies_using_get**
> PagedResponseOfTableDto get_dependencies_using_get(query_id, limit=limit, cursor=cursor, offset=offset)

Retrieve dependencies

Returns an unordered collection of all tables the matching query uses as datasources, including any shared tables outside of this OAuth token's workspace. The endpoint verifies the user has read permissions on the query, but _not_ on the tables returned.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique identifier of the query
limit = 56 # int | The number of dependencies to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve dependencies
    api_response = api_instance.get_dependencies_using_get(query_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->get_dependencies_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique identifier of the query | 
 **limit** | **int**| The number of dependencies to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfTableDto**](PagedResponseOfTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_column_data_using_post**
> BaseResponseOfQueryColumnDataDto get_query_column_data_using_post(query_text_dto)

Retrieve query column data

Returns a QueryColumnDataDto representing the column data for the given query text. If the query isn't valid, returns a 400.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_text_dto = swagger_client.QueryTextDto() # QueryTextDto | The query text to parse, up to 30000 characters; must not be null or empty

try:
    # Retrieve query column data
    api_response = api_instance.get_query_column_data_using_post(query_text_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->get_query_column_data_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_text_dto** | [**QueryTextDto**](QueryTextDto.md)| The query text to parse, up to 30000 characters; must not be null or empty | 

### Return type

[**BaseResponseOfQueryColumnDataDto**](BaseResponseOfQueryColumnDataDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_result_using_get**
> BaseResponseOfQueryResultDto get_query_result_using_get(query_result_id)

Retrieve a single query result

Returns a single query result that matches the provided ID, or a 404 if no such query result is found.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_result_id = 'query_result_id_example' # str | The unique identifier of the query result

try:
    # Retrieve a single query result
    api_response = api_instance.get_query_result_using_get(query_result_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->get_query_result_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_result_id** | **str**| The unique identifier of the query result | 

### Return type

[**BaseResponseOfQueryResultDto**](BaseResponseOfQueryResultDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_query_using_get**
> BaseResponseOfQueryDto get_query_using_get(query_id)

Retrieve a single query

Returns a query that matches the provided ID, or a 404 if no matching query is found.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique identifier of the query

try:
    # Retrieve a single query
    api_response = api_instance.get_query_using_get(query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->get_query_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique identifier of the query | 

### Return type

[**BaseResponseOfQueryDto**](BaseResponseOfQueryDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tables_dependent_on_query_using_get**
> PagedResponseOfTableDto get_tables_dependent_on_query_using_get(query_id, limit=limit, cursor=cursor, offset=offset)

Retrieve a list of dependents

Returns a list of all tables that use the query with provided ID as a datasource. 

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique identifier of the query
limit = 56 # int | The number of folders to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of dependents
    api_response = api_instance.get_tables_dependent_on_query_using_get(query_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->get_tables_dependent_on_query_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique identifier of the query | 
 **limit** | **int**| The number of folders to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfTableDto**](PagedResponseOfTableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **is_query_valid_using_post**
> BaseResponseOfQueryDto is_query_valid_using_post(query_dto=query_dto)

Parses the query to determine if it is valid

Returns the provided QueryDto

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_dto = swagger_client.QueryDto() # QueryDto | The representation of the created query (optional)

try:
    # Parses the query to determine if it is valid
    api_response = api_instance.is_query_valid_using_post(query_dto=query_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->is_query_valid_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_dto** | [**QueryDto**](QueryDto.md)| The representation of the created query | [optional] 

### Return type

[**BaseResponseOfQueryDto**](BaseResponseOfQueryDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_queries_using_get**
> PagedResponseOfQueryDto list_queries_using_get(limit=limit, cursor=cursor, offset=offset)

Retrieve list of queries

Returns a list of all non-temporary queries associated with the workspace. By default, these queries are ordered by their names, in ascending order.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of queries to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve list of queries
    api_response = api_instance.list_queries_using_get(limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->list_queries_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of queries to return, from 1 to 1000; by default, 1000 | [optional] 
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

# **list_query_results_using_get**
> PagedResponseOfQueryResultDto list_query_results_using_get(query_id=query_id, cursor=cursor, limit=limit, offset=offset)

Retrieve a list of query results

Returns a paged list of query results that match the provided query ID, or an empty list if no matching query is found.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique identifier of the query (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
limit = 1000 # int | The number of query results to return, from 1 to 1000; by default, 1000 (optional) (default to 1000)
offset = 0 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional) (default to 0)

try:
    # Retrieve a list of query results
    api_response = api_instance.list_query_results_using_get(query_id=query_id, cursor=cursor, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->list_query_results_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique identifier of the query | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **limit** | **int**| The number of query results to return, from 1 to 1000; by default, 1000 | [optional] [default to 1000]
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] [default to 0]

### Return type

[**PagedResponseOfQueryResultDto**](PagedResponseOfQueryResultDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **preview_query_using_post**
> BaseResponseOfQueryDto preview_query_using_post(table_id, limit=limit, file_name=file_name)

Preview a query

Creates a limited scope query object, but does _not_ execute it. The query selects all values against the provided table, up to 10 rows. This endpoint may allow unpermissioned users to preview table data; full permissions to datasources are _not_ validated.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
table_id = 'table_id_example' # str | The identifier of the table to query
limit = 56 # int | The number of rows to return (optional)
file_name = 'file_name_example' # str | The name of the file to create (optional)

try:
    # Preview a query
    api_response = api_instance.preview_query_using_post(table_id, limit=limit, file_name=file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->preview_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **table_id** | **str**| The identifier of the table to query | 
 **limit** | **int**| The number of rows to return | [optional] 
 **file_name** | **str**| The name of the file to create | [optional] 

### Return type

[**BaseResponseOfQueryDto**](BaseResponseOfQueryDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_query_using_post**
> BaseResponseOfQueryResultDto run_query_using_post(query_result_dto=query_result_dto)

Execute a query

Runs a query and immediately returns a query result entity, which has an ID that can be used to poll the status from the GET /queryresult method. A status of COMPLETED or ERROR indicates the query has completed.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_result_dto = swagger_client.QueryResultDto() # QueryResultDto | The representation of the created query (optional)

try:
    # Execute a query
    api_response = api_instance.run_query_using_post(query_result_dto=query_result_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->run_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_result_dto** | [**QueryResultDto**](QueryResultDto.md)| The representation of the created query | [optional] 

### Return type

[**BaseResponseOfQueryResultDto**](BaseResponseOfQueryResultDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_query_using_put**
> BaseResponseOfQueryDto update_query_using_put(query_id, query_dto=query_dto)

Update a single query

Updates the query that matches the provided ID with the details provided in the body.

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
api_instance = swagger_client.QueryManagementApi(swagger_client.ApiClient(configuration))
query_id = 'query_id_example' # str | The unique identifier of the query
query_dto = swagger_client.QueryDto() # QueryDto | The representation of the query to update (optional)

try:
    # Update a single query
    api_response = api_instance.update_query_using_put(query_id, query_dto=query_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling QueryManagementApi->update_query_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_id** | **str**| The unique identifier of the query | 
 **query_dto** | [**QueryDto**](QueryDto.md)| The representation of the query to update | [optional] 

### Return type

[**BaseResponseOfQueryDto**](BaseResponseOfQueryDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

