# openapi_client.ServiceContractsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_contract_order_by_fields_using_get**](ServiceContractsApi.md#get_service_contract_order_by_fields_using_get) | **GET** /alias/{alias}/protected/servicecontracts/orderbyfields | Get possible fields for orderby of servicecontract fields
[**get_service_contract_using_get**](ServiceContractsApi.md#get_service_contract_using_get) | **GET** /alias/{alias}/protected/servicecontracts/{id} | Get one specific servicecontract by id
[**search_service_contracts_using_post**](ServiceContractsApi.md#search_service_contracts_using_post) | **POST** /alias/{alias}/protected/servicecontracts/search | Get a list of servicecontracts


# **get_service_contract_order_by_fields_using_get**
> [str] get_service_contract_order_by_fields_using_get(alias)

Get possible fields for orderby of servicecontract fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import service_contracts_api
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
    api_instance = service_contracts_api.ServiceContractsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of servicecontract fields
        api_response = api_instance.get_service_contract_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServiceContractsApi->get_service_contract_order_by_fields_using_get: %s\n" % e)
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

# **get_service_contract_using_get**
> ServiceContract get_service_contract_using_get(alias, id)

Get one specific servicecontract by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import service_contracts_api
from openapi_client.model.service_contract import ServiceContract
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
    api_instance = service_contracts_api.ServiceContractsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific servicecontract by id
        api_response = api_instance.get_service_contract_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServiceContractsApi->get_service_contract_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ServiceContract**](ServiceContract.md)

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

# **search_service_contracts_using_post**
> ListResultWrapperServiceContract search_service_contracts_using_post(alias, servicecontract_search_query)

Get a list of servicecontracts

Get a list of servicecontracts  by a search query, paging is used, specify limit and page; Model Type: ServiceContract is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import service_contracts_api
from openapi_client.model.service_contract_search_query import ServiceContractSearchQuery
from openapi_client.model.list_result_wrapper_service_contract import ListResultWrapperServiceContract
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
    api_instance = service_contracts_api.ServiceContractsApi(api_client)
    alias = "alias_example" # str | alias
    servicecontract_search_query = ServiceContractSearchQuery(
        article_id="article_id_example",
        customer_ids=[
            "customer_ids_example",
        ],
        end_date_from=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        end_date_to=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        numbers=[
            "numbers_example",
        ],
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        start_date_from=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        start_date_to=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        treatment_ids=[
            "treatment_ids_example",
        ],
    ) # ServiceContractSearchQuery | servicecontractSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of servicecontracts
        api_response = api_instance.search_service_contracts_using_post(alias, servicecontract_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ServiceContractsApi->search_service_contracts_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **servicecontract_search_query** | [**ServiceContractSearchQuery**](ServiceContractSearchQuery.md)| servicecontractSearchQuery |

### Return type

[**ListResultWrapperServiceContract**](ListResultWrapperServiceContract.md)

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

