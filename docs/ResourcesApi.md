# openapi_client.ResourcesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_resource_using_post**](ResourcesApi.md#create_resource_using_post) | **POST** /alias/{alias}/protected/resources | Create a new resource
[**delete_resource_using_delete**](ResourcesApi.md#delete_resource_using_delete) | **DELETE** /alias/{alias}/protected/resources/{id} | Delete a resource with given id, only resources which have no future appointments could be deleted
[**get_resource_using_get**](ResourcesApi.md#get_resource_using_get) | **GET** /alias/{alias}/protected/resources/{id} | Get one specific resource by id
[**search_resources_using_post**](ResourcesApi.md#search_resources_using_post) | **POST** /alias/{alias}/protected/resources/search | Get a list of resources
[**update_resource_using_patch**](ResourcesApi.md#update_resource_using_patch) | **PATCH** /alias/{alias}/protected/resources/{id} | Update resource with given id


# **create_resource_using_post**
> CreationResponse create_resource_using_post(alias, to_save)

Create a new resource

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import resources_api
from openapi_client.model.creation_response import CreationResponse
from openapi_client.model.resource_to_save import ResourceToSave
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
    api_instance = resources_api.ResourcesApi(api_client)
    alias = "alias_example" # str | alias
    to_save = ResourceToSave(
        branch_id="branch_id_example",
        capacity=1,
        color_code="#00FF00",
        default_app_minutes=60,
        description="description_example",
        for_all_branches=False,
        hidden=False,
        name="name_example",
        staff_id="staff_id_example",
        visible_in_branches=[
            "visible_in_branches_example",
        ],
    ) # ResourceToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new resource
        api_response = api_instance.create_resource_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcesApi->create_resource_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**ResourceToSave**](ResourceToSave.md)| toSave |

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

# **delete_resource_using_delete**
> delete_resource_using_delete(alias, id)

Delete a resource with given id, only resources which have no future appointments could be deleted

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import resources_api
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
    api_instance = resources_api.ResourcesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Delete a resource with given id, only resources which have no future appointments could be deleted
        api_instance.delete_resource_using_delete(alias, id)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcesApi->delete_resource_using_delete: %s\n" % e)
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

# **get_resource_using_get**
> Resource get_resource_using_get(alias, id)

Get one specific resource by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import resources_api
from openapi_client.model.resource import Resource
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
    api_instance = resources_api.ResourcesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific resource by id
        api_response = api_instance.get_resource_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcesApi->get_resource_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Resource**](Resource.md)

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

# **search_resources_using_post**
> ListResultWrapperResource search_resources_using_post(alias, resource_search_query)

Get a list of resources

Get a list of resources  by a search query, paging is used, specify limit and page; Model Type: Resource is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import resources_api
from openapi_client.model.list_result_wrapper_resource import ListResultWrapperResource
from openapi_client.model.resource_search_query import ResourceSearchQuery
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
    api_instance = resources_api.ResourcesApi(api_client)
    alias = "alias_example" # str | alias
    resource_search_query = ResourceSearchQuery(
        branch_id="branch_id_example",
        for_online_booking=False,
        hidden=False,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        name="name_example",
        staff_id="staff_id_example",
    ) # ResourceSearchQuery | resourceSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of resources
        api_response = api_instance.search_resources_using_post(alias, resource_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcesApi->search_resources_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **resource_search_query** | [**ResourceSearchQuery**](ResourceSearchQuery.md)| resourceSearchQuery |

### Return type

[**ListResultWrapperResource**](ListResultWrapperResource.md)

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

# **update_resource_using_patch**
> update_resource_using_patch(alias, id, to_update)

Update resource with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import resources_api
from openapi_client.model.resource_to_save import ResourceToSave
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
    api_instance = resources_api.ResourcesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = ResourceToSave(
        branch_id="branch_id_example",
        capacity=1,
        color_code="#00FF00",
        default_app_minutes=60,
        description="description_example",
        for_all_branches=False,
        hidden=False,
        name="name_example",
        staff_id="staff_id_example",
        visible_in_branches=[
            "visible_in_branches_example",
        ],
    ) # ResourceToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update resource with given id
        api_instance.update_resource_using_patch(alias, id, to_update)
    except openapi_client.ApiException as e:
        print("Exception when calling ResourcesApi->update_resource_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**ResourceToSave**](ResourceToSave.md)| toUpdate |

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

