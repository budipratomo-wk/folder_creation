# swagger_client.TagManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_tag_using_post**](TagManagementApi.md#create_tag_using_post) | **POST** /api/v1/tag | Create a new tag
[**delete_tag_using_delete**](TagManagementApi.md#delete_tag_using_delete) | **DELETE** /api/v1/tag/{tagId} | Delete a single tag
[**list_tags_using_get**](TagManagementApi.md#list_tags_using_get) | **GET** /api/v1/tag | Retrieve a list of tags
[**update_tag_using_put**](TagManagementApi.md#update_tag_using_put) | **PUT** /api/v1/tag/{tagId} | Update a single tag


# **create_tag_using_post**
> BaseResponseOfTagDto create_tag_using_post(tag_dto=tag_dto)

Create a new tag

Creates a tag. If another tag already has the same key, returns a 409.

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
api_instance = swagger_client.TagManagementApi(swagger_client.ApiClient(configuration))
tag_dto = swagger_client.TagDto() # TagDto | The representation of the tag to create (optional)

try:
    # Create a new tag
    api_response = api_instance.create_tag_using_post(tag_dto=tag_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagManagementApi->create_tag_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_dto** | [**TagDto**](TagDto.md)| The representation of the tag to create | [optional] 

### Return type

[**BaseResponseOfTagDto**](BaseResponseOfTagDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tag_using_delete**
> BaseResponseOfstring delete_tag_using_delete(tag_id)

Delete a single tag

Deletes the tag with the provided ID. If no such tag is found, this is a no-op.

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
api_instance = swagger_client.TagManagementApi(swagger_client.ApiClient(configuration))
tag_id = 'tag_id_example' # str | The unique identifier of the tag

try:
    # Delete a single tag
    api_response = api_instance.delete_tag_using_delete(tag_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagManagementApi->delete_tag_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The unique identifier of the tag | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_tags_using_get**
> PagedResponseOfTagDto list_tags_using_get(limit=limit, cursor=cursor, offset=offset)

Retrieve a list of tags

Returns a paged list of all tags associated with the workspace of the request.

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
api_instance = swagger_client.TagManagementApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of tags to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of tags
    api_response = api_instance.list_tags_using_get(limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagManagementApi->list_tags_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of tags to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfTagDto**](PagedResponseOfTagDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tag_using_put**
> BaseResponseOfTagDto update_tag_using_put(tag_id, tag_dto=tag_dto)

Update a single tag

Updates the tag that matches the provided ID with the details provided in the body. Ignores the provided key, as keys are immutable once set.

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
api_instance = swagger_client.TagManagementApi(swagger_client.ApiClient(configuration))
tag_id = 'tag_id_example' # str | The unique identifier of the tag
tag_dto = swagger_client.TagDto() # TagDto | The representation of the tag to update (optional)

try:
    # Update a single tag
    api_response = api_instance.update_tag_using_put(tag_id, tag_dto=tag_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagManagementApi->update_tag_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag_id** | **str**| The unique identifier of the tag | 
 **tag_dto** | [**TagDto**](TagDto.md)| The representation of the tag to update | [optional] 

### Return type

[**BaseResponseOfTagDto**](BaseResponseOfTagDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

