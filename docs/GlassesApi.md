# openapi_client.GlassesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_glasses_using_get**](GlassesApi.md#get_glasses_using_get) | **GET** /alias/{alias}/protected/glasses/{id} | Get one specific glasses by id
[**search_glassess_using_post**](GlassesApi.md#search_glassess_using_post) | **POST** /alias/{alias}/protected/glasses/search | Get a list of glasses


# **get_glasses_using_get**
> GlassesCare get_glasses_using_get(alias, id)

Get one specific glasses by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import glasses_api
from openapi_client.model.glasses_care import GlassesCare
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
    api_instance = glasses_api.GlassesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific glasses by id
        api_response = api_instance.get_glasses_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlassesApi->get_glasses_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**GlassesCare**](GlassesCare.md)

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

# **search_glassess_using_post**
> ListResultWrapperGlassesCare search_glassess_using_post(alias, glasses_search_query)

Get a list of glasses

Get a list of glasses  by a search query, paging is used, specify limit and page; Model Type: Glasses is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import glasses_api
from openapi_client.model.glasses_search_query import GlassesSearchQuery
from openapi_client.model.list_result_wrapper_glasses_care import ListResultWrapperGlassesCare
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
    api_instance = glasses_api.GlassesApi(api_client)
    alias = "alias_example" # str | alias
    glasses_search_query = GlassesSearchQuery(
        customer_id="customer_id_example",
        from_date=dateutil_parser('1970-01-01').date(),
        load_treatment=True,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        to_date=dateutil_parser('1970-01-01').date(),
        treatment_id="treatment_id_example",
    ) # GlassesSearchQuery | glassesSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of glasses
        api_response = api_instance.search_glassess_using_post(alias, glasses_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling GlassesApi->search_glassess_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **glasses_search_query** | [**GlassesSearchQuery**](GlassesSearchQuery.md)| glassesSearchQuery |

### Return type

[**ListResultWrapperGlassesCare**](ListResultWrapperGlassesCare.md)

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

