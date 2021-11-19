# amparex.AppointmentsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_appointment_using_post**](AppointmentsApi.md#create_appointment_using_post) | **POST** /alias/{alias}/protected/appointments | Create a new appointment
[**delete_availability_using_delete**](AppointmentsApi.md#delete_availability_using_delete) | **DELETE** /alias/{alias}/protected/appointments/{id} | Delete an appointment with given id
[**get_appointment_order_by_fields_using_get**](AppointmentsApi.md#get_appointment_order_by_fields_using_get) | **GET** /alias/{alias}/protected/appointments/orderbyfields | Get possible fields for orderby of appointment fields
[**get_appointment_using_get**](AppointmentsApi.md#get_appointment_using_get) | **GET** /alias/{alias}/protected/appointments/{id} | Get one specific appointment by id
[**search_appointments_using_post**](AppointmentsApi.md#search_appointments_using_post) | **POST** /alias/{alias}/protected/appointments/search | Get a list of appointments
[**update_appointment_using_patch**](AppointmentsApi.md#update_appointment_using_patch) | **PATCH** /alias/{alias}/protected/appointments/{id} | Update appointment with given id


# **create_appointment_using_post**
> CreationResponse create_appointment_using_post(alias, to_save)

Create a new appointment

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointments_api
from amparex.model.creation_response import CreationResponse
from amparex.model.appointment_to_save import AppointmentToSave
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
    api_instance = appointments_api.AppointmentsApi(api_client)
    alias = "alias_example" # str | alias
    to_save = AppointmentToSave(
        allow_parallel=False,
        canceled=False,
        comment="comment_example",
        customer=CustomerToSave(
            address=AddressToSave(
                above_name="above_name_example",
                address_type="address_residence",
                below_name="CC Miller",
                city="Leinfelden-Echterdingen",
                comment="comment_example",
                country_code="DE",
                email="info@amparex.com",
                line1="line1_example",
                line2="line2_example",
                line3="line3_example",
                owner_id="0114ee9723da000000ea005056C00008",
                phone1="+49 (0) 711 21 475 - 475",
                phone1_sms=True,
                phone2="+49 (0) 711 21 475 - 475",
                phone2_sms=False,
                phone3="+49 (0) 711 21 475 - 475",
                phone3_sms=False,
                replace_name="replace_name_example",
                street="Max-Lang-Straße 24",
                web="www.amparex.com",
                zip="70771",
            ),
            advertising_flags=15,
            birthdate="1965-05-14",
            customer_nr_extern="customer_nr_extern_example",
            customer_since="2012-12-08",
            dominant_eye="side_right",
            dominant_hand="side_left",
            extension_name="von",
            first_name="Else",
            last_visit="2006-05-25",
            privacy_statement=True,
            privacy_statement_date="2018-05-25",
            resp_branch_id="0114ee95177000000003005056C00008",
            resp_staff_id="013a4f6d22dc00019671785d18fcca80",
            restricted_view=False,
            salutation="salutation_missis",
            status_id="013d79fd800d00000038ABCDEF364676",
            surname="Kling",
            title="Prof. Dr.",
        ),
        customer_id="customer_id_example",
        date="2007-03-27",
        end_time="14:46:46",
        home_visit=False,
        marketing_action_id="marketing_action_id_example",
        post_minutes=1,
        prepare_minutes=1,
        resource_ids="",
        show_as_unavailable=False,
        start_time="14:46:46",
        status_id="status_id_example",
        text="text_example",
        treatment_head_id="treatment_head_id_example",
        type_id="type_id_example",
        use_branch_id="use_branch_id_example",
        whole_day=False,
    ) # AppointmentToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new appointment
        api_response = api_instance.create_appointment_using_post(alias, to_save)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentsApi->create_appointment_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**AppointmentToSave**](AppointmentToSave.md)| toSave |

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
**201** | Created |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |
**409** | Conflict - the slot for the appointment is overbooked |  -  |
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_availability_using_delete**
> delete_availability_using_delete(alias, id)

Delete an appointment with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointments_api
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
    api_instance = appointments_api.AppointmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Delete an appointment with given id
        api_instance.delete_availability_using_delete(alias, id)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentsApi->delete_availability_using_delete: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

void (empty response body)

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_appointment_order_by_fields_using_get**
> [str] get_appointment_order_by_fields_using_get(alias)

Get possible fields for orderby of appointment fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointments_api
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
    api_instance = appointments_api.AppointmentsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of appointment fields
        api_response = api_instance.get_appointment_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentsApi->get_appointment_order_by_fields_using_get: %s\n" % e)
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

# **get_appointment_using_get**
> Appointment get_appointment_using_get(alias, id)

Get one specific appointment by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointments_api
from amparex.model.appointment import Appointment
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
    api_instance = appointments_api.AppointmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific appointment by id
        api_response = api_instance.get_appointment_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentsApi->get_appointment_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Appointment**](Appointment.md)

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

# **search_appointments_using_post**
> ListResultWrapperAppointment search_appointments_using_post(alias, appointment_search_query)

Get a list of appointments

Get a list of appointments by a search query, paging is used, specify limit and page; Model Type: Appointment is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointments_api
from amparex.model.list_result_wrapper_appointment import ListResultWrapperAppointment
from amparex.model.appointment_search_query import AppointmentSearchQuery
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
    api_instance = appointments_api.AppointmentsApi(api_client)
    alias = "alias_example" # str | alias
    appointment_search_query = AppointmentSearchQuery(
        branch_id="branch_id_example",
        customer_id="customer_id_example",
        end_time="14:34:56",
        from_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        resource_ids=[
            "resource_ids_example",
        ],
        start_time="12:34:56",
        status_id="status_id_example",
        to_date=dateutil_parser('Tue Dec 31 01:00:00 CET 2019').date(),
        treatment_id="treatment_id_example",
        type_id="type_id_example",
    ) # AppointmentSearchQuery | appointmentSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of appointments
        api_response = api_instance.search_appointments_using_post(alias, appointment_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentsApi->search_appointments_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **appointment_search_query** | [**AppointmentSearchQuery**](AppointmentSearchQuery.md)| appointmentSearchQuery |

### Return type

[**ListResultWrapperAppointment**](ListResultWrapperAppointment.md)

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

# **update_appointment_using_patch**
> update_appointment_using_patch(alias, id, to_update)

Update appointment with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointments_api
from amparex.model.appointment_to_save import AppointmentToSave
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
    api_instance = appointments_api.AppointmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = AppointmentToSave(
        allow_parallel=False,
        canceled=False,
        comment="comment_example",
        customer=CustomerToSave(
            address=AddressToSave(
                above_name="above_name_example",
                address_type="address_residence",
                below_name="CC Miller",
                city="Leinfelden-Echterdingen",
                comment="comment_example",
                country_code="DE",
                email="info@amparex.com",
                line1="line1_example",
                line2="line2_example",
                line3="line3_example",
                owner_id="0114ee9723da000000ea005056C00008",
                phone1="+49 (0) 711 21 475 - 475",
                phone1_sms=True,
                phone2="+49 (0) 711 21 475 - 475",
                phone2_sms=False,
                phone3="+49 (0) 711 21 475 - 475",
                phone3_sms=False,
                replace_name="replace_name_example",
                street="Max-Lang-Straße 24",
                web="www.amparex.com",
                zip="70771",
            ),
            advertising_flags=15,
            birthdate="1965-05-14",
            customer_nr_extern="customer_nr_extern_example",
            customer_since="2012-12-08",
            dominant_eye="side_right",
            dominant_hand="side_left",
            extension_name="von",
            first_name="Else",
            last_visit="2006-05-25",
            privacy_statement=True,
            privacy_statement_date="2018-05-25",
            resp_branch_id="0114ee95177000000003005056C00008",
            resp_staff_id="013a4f6d22dc00019671785d18fcca80",
            restricted_view=False,
            salutation="salutation_missis",
            status_id="013d79fd800d00000038ABCDEF364676",
            surname="Kling",
            title="Prof. Dr.",
        ),
        customer_id="customer_id_example",
        date="2007-03-27",
        end_time="14:46:46",
        home_visit=False,
        marketing_action_id="marketing_action_id_example",
        post_minutes=1,
        prepare_minutes=1,
        resource_ids="",
        show_as_unavailable=False,
        start_time="14:46:46",
        status_id="status_id_example",
        text="text_example",
        treatment_head_id="treatment_head_id_example",
        type_id="type_id_example",
        use_branch_id="use_branch_id_example",
        whole_day=False,
    ) # AppointmentToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update appointment with given id
        api_instance.update_appointment_using_patch(alias, id, to_update)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentsApi->update_appointment_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**AppointmentToSave**](AppointmentToSave.md)| toUpdate |

### Return type

void (empty response body)

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |
**409** | Conflict - the slot for the appointment is overbooked |  -  |
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

