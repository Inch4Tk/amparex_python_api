# amparex.LensesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lense_option_using_get**](LensesApi.md#get_lense_option_using_get) | **GET** /alias/{alias}/protected/lenseoptions/{id} | Get one specific lenseoption by id
[**get_lense_type_using_get**](LensesApi.md#get_lense_type_using_get) | **GET** /alias/{alias}/protected/lensetypes/{id} | Get one specific lensetype by id
[**search_lense_options_using_post**](LensesApi.md#search_lense_options_using_post) | **POST** /alias/{alias}/protected/lenseoptions/search | Get a list of lenseoptions
[**search_lense_types_using_post**](LensesApi.md#search_lense_types_using_post) | **POST** /alias/{alias}/protected/lensetypes/search | Get a list of lensetypes


# **get_lense_option_using_get**
> LenseOptions get_lense_option_using_get(alias, id)

Get one specific lenseoption by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import lenses_api
from amparex.model.lense_options import LenseOptions
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
    api_instance = lenses_api.LensesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific lenseoption by id
        api_response = api_instance.get_lense_option_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LensesApi->get_lense_option_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**LenseOptions**](LenseOptions.md)

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

# **get_lense_type_using_get**
> LenseType get_lense_type_using_get(alias, id)

Get one specific lensetype by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import lenses_api
from amparex.model.lense_type import LenseType
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
    api_instance = lenses_api.LensesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific lensetype by id
        api_response = api_instance.get_lense_type_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LensesApi->get_lense_type_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**LenseType**](LenseType.md)

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

# **search_lense_options_using_post**
> ListResultWrapperLenseOptions search_lense_options_using_post(alias, lenseoption_search_query)

Get a list of lenseoptions

Get a list of lenseoptions  by a search query, paging is used, specify limit and page; Model Type: LenseOption is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import lenses_api
from amparex.model.lense_option_search_query import LenseOptionSearchQuery
from amparex.model.list_result_wrapper_lense_options import ListResultWrapperLenseOptions
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
    api_instance = lenses_api.LensesApi(api_client)
    alias = "alias_example" # str | alias
    lenseoption_search_query = LenseOptionSearchQuery(
        company_id="company_id_example",
        hst_code="hst_code_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
    ) # LenseOptionSearchQuery | lenseoptionSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of lenseoptions
        api_response = api_instance.search_lense_options_using_post(alias, lenseoption_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LensesApi->search_lense_options_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **lenseoption_search_query** | [**LenseOptionSearchQuery**](LenseOptionSearchQuery.md)| lenseoptionSearchQuery |

### Return type

[**ListResultWrapperLenseOptions**](ListResultWrapperLenseOptions.md)

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

# **search_lense_types_using_post**
> ListResultWrapperLenseType search_lense_types_using_post(alias, lensetype_search_query)

Get a list of lensetypes

Get a list of lensetypes  by a search query, paging is used, specify limit and page; Model Type: LenseType is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import lenses_api
from amparex.model.list_result_wrapper_lense_type import ListResultWrapperLenseType
from amparex.model.lense_type_search_query import LenseTypeSearchQuery
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
    api_instance = lenses_api.LensesApi(api_client)
    alias = "alias_example" # str | alias
    lensetype_search_query = LenseTypeSearchQuery(
        company_id="company_id_example",
        hst_code="hst_code_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
    ) # LenseTypeSearchQuery | lensetypeSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of lensetypes
        api_response = api_instance.search_lense_types_using_post(alias, lensetype_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LensesApi->search_lense_types_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **lensetype_search_query** | [**LenseTypeSearchQuery**](LenseTypeSearchQuery.md)| lensetypeSearchQuery |

### Return type

[**ListResultWrapperLenseType**](ListResultWrapperLenseType.md)

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

