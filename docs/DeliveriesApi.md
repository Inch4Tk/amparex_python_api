# openapi_client.DeliveriesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delivery_order_by_fields_using_get**](DeliveriesApi.md#get_delivery_order_by_fields_using_get) | **GET** /alias/{alias}/protected/deliveries/orderbyfields | Get possible fields for orderby of delivery fields
[**get_delivery_using_get**](DeliveriesApi.md#get_delivery_using_get) | **GET** /alias/{alias}/protected/deliveries/{id} | Get one specific delivery by id
[**search_deliveries_using_post**](DeliveriesApi.md#search_deliveries_using_post) | **POST** /alias/{alias}/protected/deliveries/search | Get a list of deliveries


# **get_delivery_order_by_fields_using_get**
> [str] get_delivery_order_by_fields_using_get(alias)

Get possible fields for orderby of delivery fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import deliveries_api
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
    api_instance = deliveries_api.DeliveriesApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of delivery fields
        api_response = api_instance.get_delivery_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeliveriesApi->get_delivery_order_by_fields_using_get: %s\n" % e)
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

# **get_delivery_using_get**
> Delivery get_delivery_using_get(alias, id)

Get one specific delivery by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import deliveries_api
from openapi_client.model.delivery import Delivery
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
    api_instance = deliveries_api.DeliveriesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific delivery by id
        api_response = api_instance.get_delivery_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeliveriesApi->get_delivery_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Delivery**](Delivery.md)

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

# **search_deliveries_using_post**
> ListResultWrapperDelivery search_deliveries_using_post(alias, delivery_search_query)

Get a list of deliveries

Get a list of deliveries  by a search query, paging is used, specify limit and page; Model Type: Delivery is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import deliveries_api
from openapi_client.model.list_result_wrapper_delivery import ListResultWrapperDelivery
from openapi_client.model.delivery_search_query import DeliverySearchQuery
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
    api_instance = deliveries_api.DeliveriesApi(api_client)
    alias = "alias_example" # str | alias
    delivery_search_query = DeliverySearchQuery(
        delivery_nr="delivery_nr_example",
        delivery_type="delivery_type_storage",
        from_delivery_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        from_delivery_note_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        from_person_id="0115124dc15000000003005056C00008",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        to_delivery_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        to_delivery_note_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        to_person_id="0115124dc15000000003005056C00008",
        tracking_number="tracking_number_example",
    ) # DeliverySearchQuery | deliverySearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of deliveries
        api_response = api_instance.search_deliveries_using_post(alias, delivery_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling DeliveriesApi->search_deliveries_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **delivery_search_query** | [**DeliverySearchQuery**](DeliverySearchQuery.md)| deliverySearchQuery |

### Return type

[**ListResultWrapperDelivery**](ListResultWrapperDelivery.md)

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

