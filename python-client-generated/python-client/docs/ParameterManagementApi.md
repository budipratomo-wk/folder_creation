# swagger_client.ParameterManagementApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_parameter_using_post**](ParameterManagementApi.md#create_parameter_using_post) | **POST** /api/v1/parameter | Create parameter
[**delete_parameter_using_delete**](ParameterManagementApi.md#delete_parameter_using_delete) | **DELETE** /api/v1/parameter/{parameterId} | Delete Parameter
[**get_parameter_using_get**](ParameterManagementApi.md#get_parameter_using_get) | **GET** /api/v1/parameter/{parameterId} | Get Parameter
[**list_parameters_using_get**](ParameterManagementApi.md#list_parameters_using_get) | **GET** /api/v1/parameter | Get Parameters
[**update_parameter_using_put**](ParameterManagementApi.md#update_parameter_using_put) | **PUT** /api/v1/parameter/{parameterId} | Update Parameter


# **create_parameter_using_post**
> BaseResponseOfGlobalParameterDto create_parameter_using_post(parameter_dto=parameter_dto)

Create parameter

Creates a parameter.  If there is a parameter with the same ID, a 409 is returned.

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
api_instance = swagger_client.ParameterManagementApi(swagger_client.ApiClient(configuration))
parameter_dto = swagger_client.GlobalParameterDto() # GlobalParameterDto | The representation of the parameter to create (optional)

try:
    # Create parameter
    api_response = api_instance.create_parameter_using_post(parameter_dto=parameter_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterManagementApi->create_parameter_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_dto** | [**GlobalParameterDto**](GlobalParameterDto.md)| The representation of the parameter to create | [optional] 

### Return type

[**BaseResponseOfGlobalParameterDto**](BaseResponseOfGlobalParameterDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_parameter_using_delete**
> BaseResponseOfstring delete_parameter_using_delete(parameter_id)

Delete Parameter

Deletes the parameter with the provided parameter ID.  If the parameter is not found, this is a no-op.

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
api_instance = swagger_client.ParameterManagementApi(swagger_client.ApiClient(configuration))
parameter_id = 'parameter_id_example' # str | The unique identifier of the parameter

try:
    # Delete Parameter
    api_response = api_instance.delete_parameter_using_delete(parameter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterManagementApi->delete_parameter_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_id** | **str**| The unique identifier of the parameter | 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parameter_using_get**
> BaseResponseOfGlobalParameterDto get_parameter_using_get(parameter_id)

Get Parameter

Returns a parameter matching the provided parameter ID.  If no matching entity can be found, a 404 status is returned.

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
api_instance = swagger_client.ParameterManagementApi(swagger_client.ApiClient(configuration))
parameter_id = 'parameter_id_example' # str | The unique identifier of the parameter

try:
    # Get Parameter
    api_response = api_instance.get_parameter_using_get(parameter_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterManagementApi->get_parameter_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_id** | **str**| The unique identifier of the parameter | 

### Return type

[**BaseResponseOfGlobalParameterDto**](BaseResponseOfGlobalParameterDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_parameters_using_get**
> PagedResponseOfGlobalParameterDto list_parameters_using_get(limit=limit, cursor=cursor, offset=offset)

Get Parameters

Returns a list of all parameters associated with the workspace.  By default, these parameters are ordered by their names in ascending order.

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
api_instance = swagger_client.ParameterManagementApi(swagger_client.ApiClient(configuration))
limit = 56 # int | The number of parameters to return, must be between 1 and 1000, will default to 1000 (optional)
cursor = 'cursor_example' # str | A paging cursor; if included the limit is ignored (optional)
offset = 789 # int | The item to start with on the page, must be greater than or equal to 0, will default to 0 (optional)

try:
    # Get Parameters
    api_response = api_instance.list_parameters_using_get(limit=limit, cursor=cursor, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterManagementApi->list_parameters_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The number of parameters to return, must be between 1 and 1000, will default to 1000 | [optional] 
 **cursor** | **str**| A paging cursor; if included the limit is ignored | [optional] 
 **offset** | **int**| The item to start with on the page, must be greater than or equal to 0, will default to 0 | [optional] 

### Return type

[**PagedResponseOfGlobalParameterDto**](PagedResponseOfGlobalParameterDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_parameter_using_put**
> BaseResponseOfGlobalParameterDto update_parameter_using_put(parameter_id, parameter_dto=parameter_dto)

Update Parameter

Updates the parameter matching the provided ID in the provided payload.

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
api_instance = swagger_client.ParameterManagementApi(swagger_client.ApiClient(configuration))
parameter_id = 'parameter_id_example' # str | The unique identifier of the parameter
parameter_dto = swagger_client.GlobalParameterDto() # GlobalParameterDto | The representation of the parameter to update (optional)

try:
    # Update Parameter
    api_response = api_instance.update_parameter_using_put(parameter_id, parameter_dto=parameter_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ParameterManagementApi->update_parameter_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parameter_id** | **str**| The unique identifier of the parameter | 
 **parameter_dto** | [**GlobalParameterDto**](GlobalParameterDto.md)| The representation of the parameter to update | [optional] 

### Return type

[**BaseResponseOfGlobalParameterDto**](BaseResponseOfGlobalParameterDto.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

