# swagger_client.APIHealthApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**health_check_using_get**](APIHealthApi.md#health_check_using_get) | **GET** /health | Health check


# **health_check_using_get**
> BaseResponseOfMapOfstringAndstring health_check_using_get()

Health check

Returns the status of the API WSGI servers

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.APIHealthApi()

try:
    # Health check
    api_response = api_instance.health_check_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling APIHealthApi->health_check_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**BaseResponseOfMapOfstringAndstring**](BaseResponseOfMapOfstringAndstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

