# amparex.ColorsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_color_using_get**](ColorsApi.md#get_color_using_get) | **GET** /alias/{alias}/protected/colors/{id} | Get one specific color by id
[**search_colors_using_post**](ColorsApi.md#search_colors_using_post) | **POST** /alias/{alias}/protected/colors/search | Get a list of colors


# **get_color_using_get**
> Color get_color_using_get(alias, id)

Get one specific color by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import colors_api
from amparex.model.color import Color
from pprint import pprint
# Defining the host is optional and defaults to http://trial.amparex.net:8078/amparex/webaxapi
# See configuration.py for a list of all supported configuration parameters.
configuration = amparex.Configuration(
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
with amparex.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colors_api.ColorsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific color by id
        api_response = api_instance.get_color_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ColorsApi->get_color_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Color**](Color.md)

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

# **search_colors_using_post**
> ListResultWrapperColor search_colors_using_post(alias, search_query)

Get a list of colors

Get a list of colors by a search query, paging is used, specify limit and page; Model Type: Color is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import colors_api
from amparex.model.color_search_query import ColorSearchQuery
from amparex.model.list_result_wrapper_color import ListResultWrapperColor
from pprint import pprint
# Defining the host is optional and defaults to http://trial.amparex.net:8078/amparex/webaxapi
# See configuration.py for a list of all supported configuration parameters.
configuration = amparex.Configuration(
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
with amparex.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = colors_api.ColorsApi(api_client)
    alias = "alias_example" # str | alias
    search_query = ColorSearchQuery(
        hidden=False,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        name="name_example",
        only_base_color=False,
        producer_id="producer_id_example",
    ) # ColorSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of colors
        api_response = api_instance.search_colors_using_post(alias, search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ColorsApi->search_colors_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**ColorSearchQuery**](ColorSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperColor**](ListResultWrapperColor.md)

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

