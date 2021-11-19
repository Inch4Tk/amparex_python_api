# amparex.MarketingActionsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_marketing_action_order_by_fields_using_get**](MarketingActionsApi.md#get_marketing_action_order_by_fields_using_get) | **GET** /alias/{alias}/protected/marketingactions/orderbyfields | Get possible fields for orderby of marketingaction fields
[**get_marketing_action_using_get**](MarketingActionsApi.md#get_marketing_action_using_get) | **GET** /alias/{alias}/protected/marketingactions/{id} | Get one specific marketingaction by id
[**search_marketing_actions_using_post**](MarketingActionsApi.md#search_marketing_actions_using_post) | **POST** /alias/{alias}/protected/marketingactions/search | Get a list of marketingactions


# **get_marketing_action_order_by_fields_using_get**
> [str] get_marketing_action_order_by_fields_using_get(alias)

Get possible fields for orderby of marketingaction fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import marketing_actions_api
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
    api_instance = marketing_actions_api.MarketingActionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of marketingaction fields
        api_response = api_instance.get_marketing_action_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling MarketingActionsApi->get_marketing_action_order_by_fields_using_get: %s\n" % e)
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

# **get_marketing_action_using_get**
> MarketingAction get_marketing_action_using_get(alias, id)

Get one specific marketingaction by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import marketing_actions_api
from amparex.model.marketing_action import MarketingAction
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
    api_instance = marketing_actions_api.MarketingActionsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific marketingaction by id
        api_response = api_instance.get_marketing_action_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling MarketingActionsApi->get_marketing_action_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**MarketingAction**](MarketingAction.md)

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

# **search_marketing_actions_using_post**
> ListResultWrapperMarketingAction search_marketing_actions_using_post(alias, marketingaction_search_query)

Get a list of marketingactions

Get a list of marketingactions  by a search query, paging is used, specify limit and page; Model Type: MarketingAction is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import marketing_actions_api
from amparex.model.marketing_action_search_query import MarketingActionSearchQuery
from amparex.model.list_result_wrapper_marketing_action import ListResultWrapperMarketingAction
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
    api_instance = marketing_actions_api.MarketingActionsApi(api_client)
    alias = "alias_example" # str | alias
    marketingaction_search_query = MarketingActionSearchQuery(
        end_date=dateutil_parser('1970-01-01').date(),
        ident_code="ident_code_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        name="name_example",
        not_for_new_customers=False,
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        short_name="short_name_example",
        start_date=dateutil_parser('1970-01-01').date(),
        system=False,
    ) # MarketingActionSearchQuery | marketingactionSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of marketingactions
        api_response = api_instance.search_marketing_actions_using_post(alias, marketingaction_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling MarketingActionsApi->search_marketing_actions_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **marketingaction_search_query** | [**MarketingActionSearchQuery**](MarketingActionSearchQuery.md)| marketingactionSearchQuery |

### Return type

[**ListResultWrapperMarketingAction**](ListResultWrapperMarketingAction.md)

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

