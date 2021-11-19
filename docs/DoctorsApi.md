# amparex.DoctorsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_doctor_order_by_fields_using_get**](DoctorsApi.md#get_doctor_order_by_fields_using_get) | **GET** /alias/{alias}/protected/doctors/orderbyfields | Get possible fields for orderby of doctor fields
[**get_doctor_using_get**](DoctorsApi.md#get_doctor_using_get) | **GET** /alias/{alias}/protected/doctors/{id} | Get one specific doctor by id
[**search_doctors_using_post**](DoctorsApi.md#search_doctors_using_post) | **POST** /alias/{alias}/protected/doctors/search | Get a list of doctors


# **get_doctor_order_by_fields_using_get**
> [str] get_doctor_order_by_fields_using_get(alias)

Get possible fields for orderby of doctor fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import doctors_api
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
    api_instance = doctors_api.DoctorsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of doctor fields
        api_response = api_instance.get_doctor_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling DoctorsApi->get_doctor_order_by_fields_using_get: %s\n" % e)
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

# **get_doctor_using_get**
> Doctor get_doctor_using_get(alias, id)

Get one specific doctor by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import doctors_api
from amparex.model.doctor import Doctor
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
    api_instance = doctors_api.DoctorsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific doctor by id
        api_response = api_instance.get_doctor_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling DoctorsApi->get_doctor_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Doctor**](Doctor.md)

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

# **search_doctors_using_post**
> ListResultWrapperDoctor search_doctors_using_post(alias, doctor_search_query)

Get a list of doctors

Get a list of doctors  by a search query, paging is used, specify limit and page; Model Type: Doctor is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import doctors_api
from amparex.model.list_result_wrapper_doctor import ListResultWrapperDoctor
from amparex.model.doctor_search_query import DoctorSearchQuery
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
    api_instance = doctors_api.DoctorsApi(api_client)
    alias = "alias_example" # str | alias
    doctor_search_query = DoctorSearchQuery(
        birthdate=dateutil_parser('1970-01-01').date(),
        business_name="business_name_example",
        business_premises_number="business_premises_number_example",
        dentist=True,
        doctor_number="doctor_number_example",
        doctor_seq_nr=1,
        firstname="firstname_example",
        ik_number="ik_number_example",
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
        post_nominal="post_nominal_example",
        surname="surname_example",
        used=True,
    ) # DoctorSearchQuery | doctorSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of doctors
        api_response = api_instance.search_doctors_using_post(alias, doctor_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling DoctorsApi->search_doctors_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **doctor_search_query** | [**DoctorSearchQuery**](DoctorSearchQuery.md)| doctorSearchQuery |

### Return type

[**ListResultWrapperDoctor**](ListResultWrapperDoctor.md)

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

