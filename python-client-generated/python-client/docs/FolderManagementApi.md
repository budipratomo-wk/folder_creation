# swagger_client.FolderManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_folder_using_post**](FolderManagementApi.md#create_folder_using_post) | **POST** /api/v1/folder | Create a new folder
[**delete_folder_using_delete**](FolderManagementApi.md#delete_folder_using_delete) | **DELETE** /api/v1/folder/{folderId} | Delete a single folder
[**get_folder_using_get**](FolderManagementApi.md#get_folder_using_get) | **GET** /api/v1/folder/{folderId} | Retrieve a single folder
[**list_children_using_get**](FolderManagementApi.md#list_children_using_get) | **GET** /api/v1/folder/{folderId}/children | Retrieve list of folder contents
[**list_folders_using_get**](FolderManagementApi.md#list_folders_using_get) | **GET** /api/v1/folder | Retrieve a list of folders
[**search_using_get**](FolderManagementApi.md#search_using_get) | **GET** /api/v1/entity | Search
[**set_children_using_post**](FolderManagementApi.md#set_children_using_post) | **POST** /api/v1/folder/{folderId}/children | Move content into a folder
[**update_folder_using_put**](FolderManagementApi.md#update_folder_using_put) | **PUT** /api/v1/folder/{folderId} | Update a single folder


# **create_folder_using_post**
> BaseResponseOfFolderDto create_folder_using_post(folder_dto=folder_dto)

Create a new folder

Creates a folder using the provided information and returns the folder meta.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
folder_dto = swagger_client.FolderDto() # FolderDto | The representation of the folder to create (optional)

try:
    # Create a new folder
    api_response = api_instance.create_folder_using_post(folder_dto=folder_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->create_folder_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_dto** | [**FolderDto**](FolderDto.md)| The representation of the folder to create | [optional] 

### Return type

[**BaseResponseOfFolderDto**](BaseResponseOfFolderDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_folder_using_delete**
> BaseResponseOfstring delete_folder_using_delete(folder_id)

Delete a single folder

Deletes the folder with the provided ID.  If the folder is not found, this is a no-op. <b>All files and sub-folders are also recursively deleted.</b>

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
folder_id = 'folder_id_example' # str | The unique identifier of the folder

try:
    # Delete a single folder
    api_response = api_instance.delete_folder_using_delete(folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->delete_folder_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The unique identifier of the folder | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_folder_using_get**
> BaseResponseOfFolderDto get_folder_using_get(folder_id)

Retrieve a single folder

Returns a folder with the provided ID, or a 404 if no matching folder is found.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
folder_id = 'folder_id_example' # str | The unique identifier of the folder

try:
    # Retrieve a single folder
    api_response = api_instance.get_folder_using_get(folder_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->get_folder_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The unique identifier of the folder | 

### Return type

[**BaseResponseOfFolderDto**](BaseResponseOfFolderDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_children_using_get**
> PagedResponseOfFolderableDto list_children_using_get(folder_id, limit=limit, cursor=cursor, offset=offset)

Retrieve list of folder contents

Returns a paged list of all children whose parent ID matches the provided folder ID.  If the folder ID in the path is the literal 'null' value, returns a list of all entities with no parent.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
folder_id = 'folder_id_example' # str | The unique identifier of the folder
limit = 56 # int | The number of folders to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve list of folder contents
    api_response = api_instance.list_children_using_get(folder_id, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->list_children_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The unique identifier of the folder | 
 **limit** | **int**| The number of folders to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfFolderableDto**](PagedResponseOfFolderableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_folders_using_get**
> PagedResponseOfFolderDto list_folders_using_get(limit=limit, cursor=cursor, offset=offset)

Retrieve a list of folders

Returns a paged list of all folders associated with the workspace.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of folders to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Retrieve a list of folders
    api_response = api_instance.list_folders_using_get(limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->list_folders_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of folders to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfFolderDto**](PagedResponseOfFolderDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_using_get**
> PagedResponseOfFolderableDto search_using_get(name=name, description=description, type=type, limit=limit, cursor=cursor, offset=offset)

Search

Returns a list of all entities that match the provided criteria. Both name and description are fuzzy matches; they match _any_ entity that contains the provided string. The type is used to filter results based on the provided type of entity.  The consumer must have READ access on all returned entities.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
name = 'name_example' # str | The name to use when fuzzy-matching entities (optional)
description = 'description_example' # str | The description to use when fuzzy-matching entities (optional)
type = [56] # list[int] | To limit the scope, the type of entity to return in the results (optional)
limit = 56 # int | The number of folders to return, from 1 to 1000; by default, 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included, `limit` is ignored (optional)
offset = 789 # int | The item to start with on the page, greater than or equal to 0; by default, 0 (optional)

try:
    # Search
    api_response = api_instance.search_using_get(name=name, description=description, type=type, limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->search_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name to use when fuzzy-matching entities | [optional] 
 **description** | **str**| The description to use when fuzzy-matching entities | [optional] 
 **type** | [**list[int]**](int.md)| To limit the scope, the type of entity to return in the results | [optional] 
 **limit** | **int**| The number of folders to return, from 1 to 1000; by default, 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included, &#x60;limit&#x60; is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, greater than or equal to 0; by default, 0 | [optional] 

### Return type

[**PagedResponseOfFolderableDto**](PagedResponseOfFolderableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_children_using_post**
> BaseResponseOfCollectionOfFolderableDto set_children_using_post(folder_id, children=children)

Move content into a folder

Sets the children of a folder using the entities' types and IDs provided in the body. If the entities previously resided under a folder, including the root, they move to the folder with the provided ID. If the provided ID is 'null', the entities move to the root folder.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
folder_id = 'folder_id_example' # str | The unique identifier of the folder
children = [swagger_client.FolderableDto()] # list[FolderableDto] | The representation of the entities to drop into the folder (optional)

try:
    # Move content into a folder
    api_response = api_instance.set_children_using_post(folder_id, children=children)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->set_children_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The unique identifier of the folder | 
 **children** | [**list[FolderableDto]**](FolderableDto.md)| The representation of the entities to drop into the folder | [optional] 

### Return type

[**BaseResponseOfCollectionOfFolderableDto**](BaseResponseOfCollectionOfFolderableDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_folder_using_put**
> BaseResponseOfFolderDto update_folder_using_put(folder_id, folder_dto=folder_dto)

Update a single folder

Updates the folder that matches the provided ID with the details provided in the body.

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
api_instance = swagger_client.FolderManagementApi(swagger_client.ApiClient(configuration))
folder_id = 'folder_id_example' # str | The unique identifier of the folder
folder_dto = swagger_client.FolderDto() # FolderDto | The representation of the folder to update (optional)

try:
    # Update a single folder
    api_response = api_instance.update_folder_using_put(folder_id, folder_dto=folder_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling FolderManagementApi->update_folder_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**| The unique identifier of the folder | 
 **folder_dto** | [**FolderDto**](FolderDto.md)| The representation of the folder to update | [optional] 

### Return type

[**BaseResponseOfFolderDto**](BaseResponseOfFolderDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

