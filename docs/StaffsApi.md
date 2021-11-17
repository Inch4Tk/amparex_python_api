# openapi_client.StaffsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_staff_using_post**](StaffsApi.md#create_staff_using_post) | **POST** /alias/{alias}/protected/staffs | Create a new staff
[**get_staff_using_get**](StaffsApi.md#get_staff_using_get) | **GET** /alias/{alias}/protected/staffs/{id} | Get one specific staff by id
[**search_staffs_using_post**](StaffsApi.md#search_staffs_using_post) | **POST** /alias/{alias}/protected/staffs/search | Get a list of staffs
[**update_appointment_using_patch1**](StaffsApi.md#update_appointment_using_patch1) | **PATCH** /alias/{alias}/protected/staffs/{id} | Update staff with given id


# **create_staff_using_post**
> CreationResponse create_staff_using_post(alias, to_save)

Create a new staff

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import staffs_api
from openapi_client.model.creation_response import CreationResponse
from openapi_client.model.staff_to_save import StaffToSave
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
    api_instance = staffs_api.StaffsApi(api_client)
    alias = "alias_example" # str | alias
    to_save = StaffToSave(
        birthdate="1965-03-27",
        employer_branch_id="employer_branch_id_example",
        end_date="2007-03-27",
        entry_date="2007-03-27",
        extensionname="extensionname_example",
        firstname="firstname_example",
        initials="initials_example",
        job_name="job_name_example",
        pause_minutes=1,
        post_nominal=Optionalstring(
            present=True,
        ),
        salutation="salutation_example",
        show_tip_of_the_day=False,
        signature_text="signature_text_example",
        social_security_number="social_security_number_example",
        sponsor_accounting_number="sponsor_accounting_number_example",
        staff_nr=1,
        surname="surname_example",
        title="title_example",
        vacation_days=3.14,
        work_hours="work_hours_example",
        work_hours_monthly=False,
    ) # StaffToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new staff
        api_response = api_instance.create_staff_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StaffsApi->create_staff_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**StaffToSave**](StaffToSave.md)| toSave |

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
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_staff_using_get**
> Staff get_staff_using_get(alias, id)

Get one specific staff by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import staffs_api
from openapi_client.model.staff import Staff
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
    api_instance = staffs_api.StaffsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific staff by id
        api_response = api_instance.get_staff_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StaffsApi->get_staff_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Staff**](Staff.md)

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

# **search_staffs_using_post**
> ListResultWrapperStaff search_staffs_using_post(alias, search_query)

Get a list of staffs

Get a list of staffs by a search query; Model Type: Staff is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import staffs_api
from openapi_client.model.staff_search_query import StaffSearchQuery
from openapi_client.model.list_result_wrapper_staff import ListResultWrapperStaff
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
    api_instance = staffs_api.StaffsApi(api_client)
    alias = "alias_example" # str | alias
    search_query = StaffSearchQuery(
        currently_employed=False,
        employed_in_branch="employed_in_branch_example",
        first_name="first_name_example",
        initials="initials_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        surname="surname_example",
    ) # StaffSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of staffs
        api_response = api_instance.search_staffs_using_post(alias, search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling StaffsApi->search_staffs_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**StaffSearchQuery**](StaffSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperStaff**](ListResultWrapperStaff.md)

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

# **update_appointment_using_patch1**
> update_appointment_using_patch1(alias, id, to_update)

Update staff with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import staffs_api
from openapi_client.model.staff_to_save import StaffToSave
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
    api_instance = staffs_api.StaffsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = StaffToSave(
        birthdate="1965-03-27",
        employer_branch_id="employer_branch_id_example",
        end_date="2007-03-27",
        entry_date="2007-03-27",
        extensionname="extensionname_example",
        firstname="firstname_example",
        initials="initials_example",
        job_name="job_name_example",
        pause_minutes=1,
        post_nominal=Optionalstring(
            present=True,
        ),
        salutation="salutation_example",
        show_tip_of_the_day=False,
        signature_text="signature_text_example",
        social_security_number="social_security_number_example",
        sponsor_accounting_number="sponsor_accounting_number_example",
        staff_nr=1,
        surname="surname_example",
        title="title_example",
        vacation_days=3.14,
        work_hours="work_hours_example",
        work_hours_monthly=False,
    ) # StaffToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update staff with given id
        api_instance.update_appointment_using_patch1(alias, id, to_update)
    except openapi_client.ApiException as e:
        print("Exception when calling StaffsApi->update_appointment_using_patch1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**StaffToSave**](StaffToSave.md)| toUpdate |

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
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

