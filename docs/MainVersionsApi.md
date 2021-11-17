# openapi_client.MainVersionsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_main_version_order_by_fields_using_get**](MainVersionsApi.md#get_main_version_order_by_fields_using_get) | **GET** /alias/{alias}/protected/mainversions/orderbyfields | Get possible fields for orderby of mainversion fields
[**get_main_version_using_get**](MainVersionsApi.md#get_main_version_using_get) | **GET** /alias/{alias}/protected/mainversions/{id} | Get one specific mainversion by id
[**search_main_versions_using_post**](MainVersionsApi.md#search_main_versions_using_post) | **POST** /alias/{alias}/protected/mainversions/search | Get a list of mainversions


# **get_main_version_order_by_fields_using_get**
> [str] get_main_version_order_by_fields_using_get(alias)

Get possible fields for orderby of mainversion fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import main_versions_api
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
    api_instance = main_versions_api.MainVersionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of mainversion fields
        api_response = api_instance.get_main_version_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MainVersionsApi->get_main_version_order_by_fields_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

**[str]**

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_main_version_using_get**
> MainVersion get_main_version_using_get(alias, id)

Get one specific mainversion by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import main_versions_api
from openapi_client.model.main_version import MainVersion
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
    api_instance = main_versions_api.MainVersionsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific mainversion by id
        api_response = api_instance.get_main_version_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MainVersionsApi->get_main_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**MainVersion**](MainVersion.md)

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_main_versions_using_post**
> ListResultWrapperMainVersion search_main_versions_using_post(alias, mainversion_search_query)

Get a list of mainversions

Get a list of mainversions  by a search query, paging is used, specify limit and page; Model Type: MainVersion is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import main_versions_api
from openapi_client.model.main_version_search_query import MainVersionSearchQuery
from openapi_client.model.list_result_wrapper_main_version import ListResultWrapperMainVersion
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
    api_instance = main_versions_api.MainVersionsApi(api_client)
    alias = "alias_example" # str | alias
    mainversion_search_query = MainVersionSearchQuery(
        end_date_from=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        end_date_to=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        number="number_example",
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        start_date_from=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        start_date_to=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        status="status_planned / status_released / status_unsupported",
    ) # MainVersionSearchQuery | mainversionSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of mainversions
        api_response = api_instance.search_main_versions_using_post(alias, mainversion_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling MainVersionsApi->search_main_versions_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **mainversion_search_query** | [**MainVersionSearchQuery**](MainVersionSearchQuery.md)| mainversionSearchQuery |

### Return type

[**ListResultWrapperMainVersion**](ListResultWrapperMainVersion.md)

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

