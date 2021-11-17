# openapi_client.DocumentsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_binary_using_get1**](DocumentsApi.md#get_document_binary_using_get1) | **GET** /alias/{alias}/protected/treatments/{id}/documents/{did}/binary | Get document of treatment as blob


# **get_document_binary_using_get1**
> str get_document_binary_using_get1(alias, id, did)

Get document of treatment as blob

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import documents_api
from pprint import pprint
# Defining the host is optional and defaults to http://trial.amparex.net:8078/amparex/webaxapi
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://trial.amparex.net:8078/amparex/webaxapi"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: security_token
configuration.api_key['security_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['security_token'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = documents_api.DocumentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    did = "did_example" # str | did
    image_width = 1 # int | imageWidth (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get document of treatment as blob
        api_response = api_instance.get_document_binary_using_get1(alias, id, did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_binary_using_get1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get document of treatment as blob
        api_response = api_instance.get_document_binary_using_get1(alias, id, did, image_width=image_width)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DocumentsApi->get_document_binary_using_get1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **did** | **str**| did |
 **image_width** | **int**| imageWidth | [optional]

### Return type

**str**

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

