# amparex.HearingCaresApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hearing_care_order_by_fields_using_get**](HearingCaresApi.md#get_hearing_care_order_by_fields_using_get) | **GET** /alias/{alias}/protected/hearingcares/orderbyfields | Get possible fields for orderby of hearingcare fields
[**get_hearing_care_using_get**](HearingCaresApi.md#get_hearing_care_using_get) | **GET** /alias/{alias}/protected/hearingcares/{id} | Get one specific hearingcare by id
[**search_hearing_cares_using_post**](HearingCaresApi.md#search_hearing_cares_using_post) | **POST** /alias/{alias}/protected/hearingcares/search | Get a list of hearingcares


# **get_hearing_care_order_by_fields_using_get**
> [str] get_hearing_care_order_by_fields_using_get(alias)

Get possible fields for orderby of hearingcare fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import hearing_cares_api
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
    api_instance = hearing_cares_api.HearingCaresApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of hearingcare fields
        api_response = api_instance.get_hearing_care_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling HearingCaresApi->get_hearing_care_order_by_fields_using_get: %s\n" % e)
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

# **get_hearing_care_using_get**
> HearingCare get_hearing_care_using_get(alias, id)

Get one specific hearingcare by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import hearing_cares_api
from amparex.model.hearing_care import HearingCare
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
    api_instance = hearing_cares_api.HearingCaresApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific hearingcare by id
        api_response = api_instance.get_hearing_care_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling HearingCaresApi->get_hearing_care_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**HearingCare**](HearingCare.md)

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

# **search_hearing_cares_using_post**
> ListResultWrapperHearingCare search_hearing_cares_using_post(alias, hearingcare_search_query)

Get a list of hearingcares

Get a list of hearingcares  by a search query, paging is used, specify limit and page; Model Type: HearingCare is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import hearing_cares_api
from amparex.model.list_result_wrapper_hearing_care import ListResultWrapperHearingCare
from amparex.model.hearing_care_search_query import HearingCareSearchQuery
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
    api_instance = hearing_cares_api.HearingCaresApi(api_client)
    alias = "alias_example" # str | alias
    hearingcare_search_query = HearingCareSearchQuery(
        created_from_date=dateutil_parser('1970-01-01').date(),
        created_staff_id="created_staff_id_example",
        created_to_date=dateutil_parser('1970-01-01').date(),
        customer_id="customer_id_example",
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
        treatment_head_id="treatment_head_id_example",
    ) # HearingCareSearchQuery | hearingcareSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of hearingcares
        api_response = api_instance.search_hearing_cares_using_post(alias, hearingcare_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling HearingCaresApi->search_hearing_cares_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **hearingcare_search_query** | [**HearingCareSearchQuery**](HearingCareSearchQuery.md)| hearingcareSearchQuery |

### Return type

[**ListResultWrapperHearingCare**](ListResultWrapperHearingCare.md)

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

