# swagger_client.UtilitiesApi

All URIs are relative to *https://h.app.wdesk.com/s/wdata/prep*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parse_date_using_post**](UtilitiesApi.md#parse_date_using_post) | **POST** /api/v1/util/datetime | Parse a date


# **parse_date_using_post**
> BaseResponseOfstring parse_date_using_post(datetime_dto=datetime_dto)

Parse a date

Provides a simple endpoint to check whether a given date candidate parses with the provided format string.  Both the date candidate and format strings are required. Returns a 200 if the date parses, or a 400 with a message if not. If the date parses, the provided format can be provided as column metadata, and the imported values parse correctly. The format string is java DateTimeFormatter style e.g. dateFormat = \"MM/dd/yyyy\" and candidate = \"07/28/1987\"

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
api_instance = swagger_client.UtilitiesApi(swagger_client.ApiClient(configuration))
datetime_dto = swagger_client.DatetimeDto() # DatetimeDto | The representation of the datetime object to parse (optional)

try:
    # Parse a date
    api_response = api_instance.parse_date_using_post(datetime_dto=datetime_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UtilitiesApi->parse_date_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **datetime_dto** | [**DatetimeDto**](DatetimeDto.md)| The representation of the datetime object to parse | [optional] 

### Return type

[**BaseResponseOfstring**](BaseResponseOfstring.md)

### Authorization

[oauth](../README.md#oauth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

