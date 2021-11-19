# amparex.AvailabilitiesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_availability_using_post**](AvailabilitiesApi.md#create_availability_using_post) | **POST** /alias/{alias}/protected/availabilities | Create a new availability
[**delete_availability_using_delete1**](AvailabilitiesApi.md#delete_availability_using_delete1) | **DELETE** /alias/{alias}/protected/availabilities/{id} | Delete an availability with given id
[**get_availability_order_by_fields_using_get**](AvailabilitiesApi.md#get_availability_order_by_fields_using_get) | **GET** /alias/{alias}/protected/availabilities/orderbyfields | Get possible fields for orderby of availability fields
[**get_availability_using_get**](AvailabilitiesApi.md#get_availability_using_get) | **GET** /alias/{alias}/protected/availabilities/{id} | Get one specific availability by id
[**search_availabilities_using_post**](AvailabilitiesApi.md#search_availabilities_using_post) | **POST** /alias/{alias}/protected/availabilities/search | Get a list of availabilities
[**update_availability_using_patch**](AvailabilitiesApi.md#update_availability_using_patch) | **PATCH** /alias/{alias}/protected/availabilities/{id} | Update availability with given id


# **create_availability_using_post**
> CreationResponse create_availability_using_post(alias, to_save)

Create a new availability

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import availabilities_api
from amparex.model.creation_response import CreationResponse
from amparex.model.availability_to_save import AvailabilityToSave
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
    api_instance = availabilities_api.AvailabilitiesApi(api_client)
    alias = "alias_example" # str | alias
    to_save = AvailabilityToSave(
        available=False,
        comment="comment_example",
        date="2007-03-27",
        end_time="14:46:46",
        resource_ids="",
        start_time="14:46:46",
        text="text_example",
        type_id="type_id_example",
        use_branch_id="use_branch_id_example",
    ) # AvailabilityToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new availability
        api_response = api_instance.create_availability_using_post(alias, to_save)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AvailabilitiesApi->create_availability_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**AvailabilityToSave**](AvailabilityToSave.md)| toSave |

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

# **delete_availability_using_delete1**
> delete_availability_using_delete1(alias, id)

Delete an availability with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import availabilities_api
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
    api_instance = availabilities_api.AvailabilitiesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Delete an availability with given id
        api_instance.delete_availability_using_delete1(alias, id)
    except amparex.ApiException as e:
        print("Exception when calling AvailabilitiesApi->delete_availability_using_delete1: %s\n" % e)
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

# **get_availability_order_by_fields_using_get**
> [str] get_availability_order_by_fields_using_get(alias)

Get possible fields for orderby of availability fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import availabilities_api
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
    api_instance = availabilities_api.AvailabilitiesApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of availability fields
        api_response = api_instance.get_availability_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AvailabilitiesApi->get_availability_order_by_fields_using_get: %s\n" % e)
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

# **get_availability_using_get**
> Availability get_availability_using_get(alias, id)

Get one specific availability by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import availabilities_api
from amparex.model.availability import Availability
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
    api_instance = availabilities_api.AvailabilitiesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific availability by id
        api_response = api_instance.get_availability_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AvailabilitiesApi->get_availability_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Availability**](Availability.md)

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

# **search_availabilities_using_post**
> ListResultWrapperAvailability search_availabilities_using_post(alias, availability_search_query)

Get a list of availabilities

Get a list of availabilities by a search query, paging is used, specify limit and page; Model Type: Availability is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import availabilities_api
from amparex.model.list_result_wrapper_availability import ListResultWrapperAvailability
from amparex.model.availability_search_query import AvailabilitySearchQuery
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
    api_instance = availabilities_api.AvailabilitiesApi(api_client)
    alias = "alias_example" # str | alias
    availability_search_query = AvailabilitySearchQuery(
        end_time="14:34:56",
        from_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
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
        resource_ids=[
            "resource_ids_example",
        ],
        start_time="12:34:56",
        to_date=dateutil_parser('Tue Dec 31 01:00:00 CET 2019').date(),
        type_ids=[
            "type_ids_example",
        ],
    ) # AvailabilitySearchQuery | availabilitySearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of availabilities
        api_response = api_instance.search_availabilities_using_post(alias, availability_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AvailabilitiesApi->search_availabilities_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **availability_search_query** | [**AvailabilitySearchQuery**](AvailabilitySearchQuery.md)| availabilitySearchQuery |

### Return type

[**ListResultWrapperAvailability**](ListResultWrapperAvailability.md)

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

# **update_availability_using_patch**
> update_availability_using_patch(alias, id, to_update)

Update availability with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import availabilities_api
from amparex.model.availability_to_save import AvailabilityToSave
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
    api_instance = availabilities_api.AvailabilitiesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = AvailabilityToSave(
        available=False,
        comment="comment_example",
        date="2007-03-27",
        end_time="14:46:46",
        resource_ids="",
        start_time="14:46:46",
        text="text_example",
        type_id="type_id_example",
        use_branch_id="use_branch_id_example",
    ) # AvailabilityToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update availability with given id
        api_instance.update_availability_using_patch(alias, id, to_update)
    except amparex.ApiException as e:
        print("Exception when calling AvailabilitiesApi->update_availability_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**AvailabilityToSave**](AvailabilityToSave.md)| toUpdate |

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

