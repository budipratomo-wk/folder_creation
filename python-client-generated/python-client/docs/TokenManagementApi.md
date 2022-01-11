# swagger_client.TokenManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_token_using_post**](TokenManagementApi.md#create_token_using_post) | **POST** /api/v1/token | Create a new token
[**download_file_using_get1**](TokenManagementApi.md#download_file_using_get1) | **GET** /api/v1/token/{tokenId} | Download a single file


# **create_token_using_post**
> BaseResponseOfTokenDto create_token_using_post(token_dto=token_dto)

Create a new token

Creates a temporary token—valid for only a short period of time—to download a table dataset file or query result, given its ID.

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
api_instance = swagger_client.TokenManagementApi(swagger_client.ApiClient(configuration))
token_dto = swagger_client.TokenDto() # TokenDto | The representation of the token to update (optional)

try:
    # Create a new token
    api_response = api_instance.create_token_using_post(token_dto=token_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenManagementApi->create_token_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_dto** | [**TokenDto**](TokenDto.md)| The representation of the token to update | [optional] 

### Return type

[**BaseResponseOfTokenDto**](BaseResponseOfTokenDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **download_file_using_get1**
> str download_file_using_get1(token_id, filename=filename)

Download a single file

Downloads a table dataset or query result as a file, given its token from the [`Create a new token endpoint`](ref:wdata-createtokenusingpost). If no matching entity is found, returns a 404.

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
api_instance = swagger_client.TokenManagementApi(swagger_client.ApiClient(configuration))
token_id = 'token_id_example' # str | The unique identifier of the token
filename = 'filename_example' # str | A filename for the download; if included, the default filename is overridden (optional)

try:
    # Download a single file
    api_response = api_instance.download_file_using_get1(token_id, filename=filename)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokenManagementApi->download_file_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token_id** | **str**| The unique identifier of the token | 
 **filename** | **str**| A filename for the download; if included, the default filename is overridden | [optional] 

### Return type

**str**

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

