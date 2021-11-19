# amparex.CashDeskBalancesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cash_desk_balance_using_get**](CashDeskBalancesApi.md#get_cash_desk_balance_using_get) | **GET** /alias/{alias}/protected/cashdeskbalances/{id} | Get one specific cashdeskbalance by id
[**search_cash_desk_balances_using_post**](CashDeskBalancesApi.md#search_cash_desk_balances_using_post) | **POST** /alias/{alias}/protected/cashdeskbalances/search | Get a list of cashdeskbalances


# **get_cash_desk_balance_using_get**
> ApiCashDeskBalance get_cash_desk_balance_using_get(alias, id)

Get one specific cashdeskbalance by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import cash_desk_balances_api
from amparex.model.api_cash_desk_balance import ApiCashDeskBalance
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
    api_instance = cash_desk_balances_api.CashDeskBalancesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific cashdeskbalance by id
        api_response = api_instance.get_cash_desk_balance_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling CashDeskBalancesApi->get_cash_desk_balance_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ApiCashDeskBalance**](ApiCashDeskBalance.md)

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

# **search_cash_desk_balances_using_post**
> ListResultWrapperApiCashDeskBalance search_cash_desk_balances_using_post(alias, cashdeskbalance_search_query)

Get a list of cashdeskbalances

Get a list of cashdeskbalances  by a search query, paging is used, specify limit and page; Model Type: CashDeskBalance is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import cash_desk_balances_api
from amparex.model.api_cash_desk_balance_search_query import ApiCashDeskBalanceSearchQuery
from amparex.model.list_result_wrapper_api_cash_desk_balance import ListResultWrapperApiCashDeskBalance
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
    api_instance = cash_desk_balances_api.CashDeskBalancesApi(api_client)
    alias = "alias_example" # str | alias
    cashdeskbalance_search_query = ApiCashDeskBalanceSearchQuery(
        branch_id="branch_id_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
    ) # ApiCashDeskBalanceSearchQuery | cashdeskbalanceSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of cashdeskbalances
        api_response = api_instance.search_cash_desk_balances_using_post(alias, cashdeskbalance_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling CashDeskBalancesApi->search_cash_desk_balances_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **cashdeskbalance_search_query** | [**ApiCashDeskBalanceSearchQuery**](ApiCashDeskBalanceSearchQuery.md)| cashdeskbalanceSearchQuery |

### Return type

[**ListResultWrapperApiCashDeskBalance**](ListResultWrapperApiCashDeskBalance.md)

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

