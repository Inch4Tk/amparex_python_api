# openapi_client.AppointmentPlannerApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**book_appointment_using_post**](AppointmentPlannerApi.md#book_appointment_using_post) | **POST** /alias/{alias}/protected/appointmentplanner/booking | Book appointment for template
[**get_appointment_planner_information_using_get**](AppointmentPlannerApi.md#get_appointment_planner_information_using_get) | **GET** /alias/{alias}/protected/appointmentplanner/info | Get appointment planner information
[**search_free_busy_using_post**](AppointmentPlannerApi.md#search_free_busy_using_post) | **POST** /alias/{alias}/protected/appointmentplanner/freebusy | Get a list of time slots free/busy
[**synchronize_using_post**](AppointmentPlannerApi.md#synchronize_using_post) | **POST** /alias/{alias}/protected/appointmentplanner/synchronize | Request for synchronization


# **book_appointment_using_post**
> CreationResponse book_appointment_using_post(alias, data)

Book appointment for template

Create a new appointment

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import appointment_planner_api
from openapi_client.model.book_appointment_by_template import BookAppointmentByTemplate
from openapi_client.model.creation_response import CreationResponse
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
    api_instance = appointment_planner_api.AppointmentPlannerApi(api_client)
    alias = "alias_example" # str | alias
    data = BookAppointmentByTemplate(
        branch_id="branch_id_example",
        comment="comment_example",
        customer_id="customer_id_example",
        date=dateutil_parser('Sat Jan 02 01:00:00 CET 2021').date(),
        online_booking=False,
        resource_ids=[
            "resource_ids_example",
        ],
        start_time="12:00",
        template_id="template_id_example",
    ) # BookAppointmentByTemplate | data

    # example passing only required values which don't have defaults set
    try:
        # Book appointment for template
        api_response = api_instance.book_appointment_using_post(alias, data)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppointmentPlannerApi->book_appointment_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **data** | [**BookAppointmentByTemplate**](BookAppointmentByTemplate.md)| data |

### Return type

[**CreationResponse**](CreationResponse.md)

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

# **get_appointment_planner_information_using_get**
> AppointmentPlanner get_appointment_planner_information_using_get(alias)

Get appointment planner information

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import appointment_planner_api
from openapi_client.model.appointment_planner import AppointmentPlanner
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
    api_instance = appointment_planner_api.AppointmentPlannerApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get appointment planner information
        api_response = api_instance.get_appointment_planner_information_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppointmentPlannerApi->get_appointment_planner_information_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

[**AppointmentPlanner**](AppointmentPlanner.md)

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

# **search_free_busy_using_post**
> [FreeBusyAppointment] search_free_busy_using_post(alias, search_query)

Get a list of time slots free/busy

Get a list of time slots in appointment planner

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import appointment_planner_api
from openapi_client.model.free_busy_appointment import FreeBusyAppointment
from openapi_client.model.appointment_free_busy_search_query import AppointmentFreeBusySearchQuery
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
    api_instance = appointment_planner_api.AppointmentPlannerApi(api_client)
    alias = "alias_example" # str | alias
    search_query = AppointmentFreeBusySearchQuery(
        branch_id="branch_id_example",
        duration_minutes=1,
        end_date=dateutil_parser('1970-01-01').date(),
        end_time="end_time_example",
        free_slots_only=False,
        online_booking=False,
        resource_ids=[
            "resource_ids_example",
        ],
        slice_free_slots=False,
        start_date=dateutil_parser('1970-01-01').date(),
        start_time="start_time_example",
        step_minutes=1,
        template_id="template_id_example",
    ) # AppointmentFreeBusySearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of time slots free/busy
        api_response = api_instance.search_free_busy_using_post(alias, search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppointmentPlannerApi->search_free_busy_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**AppointmentFreeBusySearchQuery**](AppointmentFreeBusySearchQuery.md)| searchQuery |

### Return type

[**[FreeBusyAppointment]**](FreeBusyAppointment.md)

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

# **synchronize_using_post**
> ResultOfSynchronization synchronize_using_post(alias, sync_request)

Request for synchronization

Ask for changes in appointment planner

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import appointment_planner_api
from openapi_client.model.request_for_synchronization import RequestForSynchronization
from openapi_client.model.result_of_synchronization import ResultOfSynchronization
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
    api_instance = appointment_planner_api.AppointmentPlannerApi(api_client)
    alias = "alias_example" # str | alias
    sync_request = RequestForSynchronization(
        availabilities=False,
        limit=1,
        resource_ids=[
            "resource_ids_example",
        ],
        sync_token="sync_token_example",
    ) # RequestForSynchronization | syncRequest

    # example passing only required values which don't have defaults set
    try:
        # Request for synchronization
        api_response = api_instance.synchronize_using_post(alias, sync_request)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AppointmentPlannerApi->synchronize_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **sync_request** | [**RequestForSynchronization**](RequestForSynchronization.md)| syncRequest |

### Return type

[**ResultOfSynchronization**](ResultOfSynchronization.md)

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

