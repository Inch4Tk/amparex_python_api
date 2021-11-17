# openapi_client.HealthInsuranceApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_health_insurance_using_get**](HealthInsuranceApi.md#get_health_insurance_using_get) | **GET** /alias/{alias}/protected/healthinsurance/{id} | Get one specific healthinsurance by id
[**search_health_insurances_using_post**](HealthInsuranceApi.md#search_health_insurances_using_post) | **POST** /alias/{alias}/protected/healthinsurance/search | Get a list of healthinsurances


# **get_health_insurance_using_get**
> HealthInsurance get_health_insurance_using_get(alias, id)

Get one specific healthinsurance by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import health_insurance_api
from openapi_client.model.health_insurance import HealthInsurance
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
    api_instance = health_insurance_api.HealthInsuranceApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific healthinsurance by id
        api_response = api_instance.get_health_insurance_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HealthInsuranceApi->get_health_insurance_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**HealthInsurance**](HealthInsurance.md)

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

# **search_health_insurances_using_post**
> ListResultWrapperHealthInsurance search_health_insurances_using_post(alias, healthinsurance_search_query)

Get a list of healthinsurances

Get a list of healthinsurances  by a search query, paging is used, specify limit and page; Model Type: HealthInsurance is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import health_insurance_api
from openapi_client.model.list_result_wrapper_health_insurance import ListResultWrapperHealthInsurance
from openapi_client.model.health_insurance_search_query import HealthInsuranceSearchQuery
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
    api_instance = health_insurance_api.HealthInsuranceApi(api_client)
    alias = "alias_example" # str | alias
    healthinsurance_search_query = HealthInsuranceSearchQuery(
        ik_number="ik_number_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        name="name_example",
        short_name="short_name_example",
    ) # HealthInsuranceSearchQuery | healthinsuranceSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of healthinsurances
        api_response = api_instance.search_health_insurances_using_post(alias, healthinsurance_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling HealthInsuranceApi->search_health_insurances_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **healthinsurance_search_query** | [**HealthInsuranceSearchQuery**](HealthInsuranceSearchQuery.md)| healthinsuranceSearchQuery |

### Return type

[**ListResultWrapperHealthInsurance**](ListResultWrapperHealthInsurance.md)

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

