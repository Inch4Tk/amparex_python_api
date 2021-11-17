# openapi_client.OrdersApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_order_using_get**](OrdersApi.md#get_order_using_get) | **GET** /alias/{alias}/protected/orders/{id} | Get one specific order by id
[**search_orders_using_post**](OrdersApi.md#search_orders_using_post) | **POST** /alias/{alias}/protected/orders/search | Get a list of orders


# **get_order_using_get**
> Order get_order_using_get(alias, id)

Get one specific order by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.order import Order
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
    api_instance = orders_api.OrdersApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific order by id
        api_response = api_instance.get_order_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->get_order_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Order**](Order.md)

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

# **search_orders_using_post**
> ListResultWrapperOrder search_orders_using_post(alias, order_search_query)

Get a list of orders

Get a list of orders  by a search query, paging is used, specify limit and page; Model Type: Order is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import orders_api
from openapi_client.model.list_result_wrapper_order import ListResultWrapperOrder
from openapi_client.model.order_search_query import OrderSearchQuery
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
    api_instance = orders_api.OrdersApi(api_client)
    alias = "alias_example" # str | alias
    order_search_query = OrderSearchQuery(
        creation_date=dateutil_parser('2019-11-05T06:35:00+01:00'),
        delivery_date=dateutil_parser('Tue Dec 31 01:00:00 CET 2019').date(),
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        order_date=dateutil_parser('2019-11-05T06:35:00+01:00'),
        order_nr="order_nr_example",
        state="order_state_closed",
        type="order_type_order",
    ) # OrderSearchQuery | orderSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of orders
        api_response = api_instance.search_orders_using_post(alias, order_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling OrdersApi->search_orders_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **order_search_query** | [**OrderSearchQuery**](OrderSearchQuery.md)| orderSearchQuery |

### Return type

[**ListResultWrapperOrder**](ListResultWrapperOrder.md)

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

