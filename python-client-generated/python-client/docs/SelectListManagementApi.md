# swagger_client.SelectListManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_select_list_using_post**](SelectListManagementApi.md#create_select_list_using_post) | **POST** /api/v1/selectlist | Create a new select list
[**delete_using_delete**](SelectListManagementApi.md#delete_using_delete) | **DELETE** /api/v1/selectlist/{selectListId} | Delete a single select list
[**get_select_list_using_get**](SelectListManagementApi.md#get_select_list_using_get) | **GET** /api/v1/selectlist/{selectListId} | Retrieve a single select list
[**list_select_lists_using_get**](SelectListManagementApi.md#list_select_lists_using_get) | **GET** /api/v1/selectlist | Retrieve a list of select lists
[**update_select_list_using_put**](SelectListManagementApi.md#update_select_list_using_put) | **PUT** /api/v1/selectlist/{selectListId} | Update a single select list


# **create_select_list_using_post**
> BaseResponseOfSelectListDto create_select_list_using_post(select_list_dto=select_list_dto)

Create a new select list

Creates a select list using the provided information and returns the select list meta.

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
api_instance = swagger_client.SelectListManagementApi(swagger_client.ApiClient(configuration))
select_list_dto = swagger_client.SelectListDto() # SelectListDto | The representation of the select list to create (optional)

try:
    # Create a new select list
    api_response = api_instance.create_select_list_using_post(select_list_dto=select_list_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelectListManagementApi->create_select_list_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_list_dto** | [**SelectListDto**](SelectListDto.md)| The representation of the select list to create | [optional] 

### Return type

[**BaseResponseOfSelectListDto**](BaseResponseOfSelectListDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete**
> BaseResponseOfstring delete_using_delete(select_list_id)

Delete a single select list

Deletes a select list with the provided ID. If no such select list exists, this is a no-op.

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
api_instance = swagger_client.SelectListManagementApi(swagger_client.ApiClient(configuration))
select_list_id = 'select_list_id_example' # str | The unique identifier of the select list

try:
    # Delete a single select list
    api_response = api_instance.delete_using_delete(select_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelectListManagementApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_list_id** | **str**| The unique identifier of the select list | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_select_list_using_get**
> BaseResponseOfSelectListDto get_select_list_using_get(select_list_id)

Retrieve a single select list

Returns a select list that matches the provided ID, or a 404 if no matching select list is found.

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
api_instance = swagger_client.SelectListManagementApi(swagger_client.ApiClient(configuration))
select_list_id = 'select_list_id_example' # str | The unique identifier of the select list

try:
    # Retrieve a single select list
    api_response = api_instance.get_select_list_using_get(select_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelectListManagementApi->get_select_list_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_list_id** | **str**| The unique identifier of the select list | 

### Return type

[**BaseResponseOfSelectListDto**](BaseResponseOfSelectListDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_select_lists_using_get**
> PagedResponseOfSelectListDto list_select_lists_using_get(limit=limit, cursor=cursor, offset=offset)

Retrieve a list of select lists

Returns a list of select lists associated with the workspace.

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
api_instance = swagger_client.SelectListManagementApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of select lists to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of select lists
    api_response = api_instance.list_select_lists_using_get(limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelectListManagementApi->list_select_lists_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of select lists to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfSelectListDto**](PagedResponseOfSelectListDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_select_list_using_put**
> BaseResponseOfSelectListDto update_select_list_using_put(select_list_dto, select_list_id)

Update a single select list

Updates the select list with the provided ID with the details provided  in the body.

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
api_instance = swagger_client.SelectListManagementApi(swagger_client.ApiClient(configuration))
select_list_dto = swagger_client.SelectListDto() # SelectListDto | The representation of the select list to update
select_list_id = 'select_list_id_example' # str | The unique identifier of the select list

try:
    # Update a single select list
    api_response = api_instance.update_select_list_using_put(select_list_dto, select_list_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SelectListManagementApi->update_select_list_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **select_list_dto** | [**SelectListDto**](SelectListDto.md)| The representation of the select list to update | 
 **select_list_id** | **str**| The unique identifier of the select list | 

### Return type

[**BaseResponseOfSelectListDto**](BaseResponseOfSelectListDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

