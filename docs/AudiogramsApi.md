# amparex.AudiogramsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_audiogram_order_by_fields_using_get**](AudiogramsApi.md#get_audiogram_order_by_fields_using_get) | **GET** /alias/{alias}/protected/audiograms/orderbyfields | Get possible fields for orderby of audiogram fields
[**get_audiogram_using_get**](AudiogramsApi.md#get_audiogram_using_get) | **GET** /alias/{alias}/protected/audiograms/{id} | Get one specific audiogram by id
[**search_audiograms_using_post**](AudiogramsApi.md#search_audiograms_using_post) | **POST** /alias/{alias}/protected/audiograms/search | Get a list of audiograms


# **get_audiogram_order_by_fields_using_get**
> [str] get_audiogram_order_by_fields_using_get(alias)

Get possible fields for orderby of audiogram fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import audiograms_api
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
    api_instance = audiograms_api.AudiogramsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of audiogram fields
        api_response = api_instance.get_audiogram_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AudiogramsApi->get_audiogram_order_by_fields_using_get: %s\n" % e)
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

# **get_audiogram_using_get**
> Audiogram get_audiogram_using_get(alias, id)

Get one specific audiogram by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import audiograms_api
from amparex.model.audiogram import Audiogram
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
    api_instance = audiograms_api.AudiogramsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific audiogram by id
        api_response = api_instance.get_audiogram_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AudiogramsApi->get_audiogram_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Audiogram**](Audiogram.md)

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

# **search_audiograms_using_post**
> ListResultWrapperAudiogram search_audiograms_using_post(alias, audiogram_search_query)

Get a list of audiograms

Get a list of audiograms  by a search query, paging is used, specify limit and page; Model Type: Audiogram is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import audiograms_api
from amparex.model.audiogram_search_query import AudiogramSearchQuery
from amparex.model.list_result_wrapper_audiogram import ListResultWrapperAudiogram
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
    api_instance = audiograms_api.AudiogramsApi(api_client)
    alias = "alias_example" # str | alias
    audiogram_search_query = AudiogramSearchQuery(
        create_date_from=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        create_date_until=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        customer_id="customer_id_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        noah_action_id="noah_action_id_example",
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        type="type_example",
    ) # AudiogramSearchQuery | audiogramSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of audiograms
        api_response = api_instance.search_audiograms_using_post(alias, audiogram_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AudiogramsApi->search_audiograms_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **audiogram_search_query** | [**AudiogramSearchQuery**](AudiogramSearchQuery.md)| audiogramSearchQuery |

### Return type

[**ListResultWrapperAudiogram**](ListResultWrapperAudiogram.md)

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

