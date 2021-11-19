# amparex.PrincipalsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_principal_using_post**](PrincipalsApi.md#create_principal_using_post) | **POST** /alias/{alias}/protected/principals | Create a new principal
[**delete_principal_using_delete**](PrincipalsApi.md#delete_principal_using_delete) | **DELETE** /alias/{alias}/protected/principals/{id} | Delete a principal with given id
[**get_principal_using_get**](PrincipalsApi.md#get_principal_using_get) | **GET** /alias/{alias}/protected/principals/{id} | Get one specific principal by id
[**search_principals_using_post**](PrincipalsApi.md#search_principals_using_post) | **POST** /alias/{alias}/protected/principals/search | Get a list of principals
[**update_principal_using_patch**](PrincipalsApi.md#update_principal_using_patch) | **PATCH** /alias/{alias}/protected/principals/{id} | Update principal with given id


# **create_principal_using_post**
> CreationResponse create_principal_using_post(alias, to_save)

Create a new principal

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import principals_api
from amparex.model.creation_response import CreationResponse
from amparex.model.principal_to_save import PrincipalToSave
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
    api_instance = principals_api.PrincipalsApi(api_client)
    alias = "alias_example" # str | alias
    to_save = PrincipalToSave(
        application_type=1,
        default_branch_id="default_branch_id_example",
        is_admin=False,
        last_password_change="2007-03-27T14:46:46",
        name="name_example",
        password="password_example",
        password_scheme="password_scheme_example",
        pincode="",
        pincode_hash="pincode_hash_example",
        principal_card_id="principal_card_id_example",
        staff_id="staff_id_example",
    ) # PrincipalToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new principal
        api_response = api_instance.create_principal_using_post(alias, to_save)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling PrincipalsApi->create_principal_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**PrincipalToSave**](PrincipalToSave.md)| toSave |

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

# **delete_principal_using_delete**
> delete_principal_using_delete(alias, id)

Delete a principal with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import principals_api
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
    api_instance = principals_api.PrincipalsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Delete a principal with given id
        api_instance.delete_principal_using_delete(alias, id)
    except amparex.ApiException as e:
        print("Exception when calling PrincipalsApi->delete_principal_using_delete: %s\n" % e)
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

# **get_principal_using_get**
> Principal get_principal_using_get(alias, id)

Get one specific principal by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import principals_api
from amparex.model.principal import Principal
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
    api_instance = principals_api.PrincipalsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific principal by id
        api_response = api_instance.get_principal_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling PrincipalsApi->get_principal_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Principal**](Principal.md)

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

# **search_principals_using_post**
> ListResultWrapperPrincipal search_principals_using_post(alias, principal_search_query)

Get a list of principals

Get a list of principals  by a search query, paging is used, specify limit and page; Model Type: Principal is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import principals_api
from amparex.model.list_result_wrapper_principal import ListResultWrapperPrincipal
from amparex.model.principal_search_query import PrincipalSearchQuery
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
    api_instance = principals_api.PrincipalsApi(api_client)
    alias = "alias_example" # str | alias
    principal_search_query = PrincipalSearchQuery(
        admin=False,
        application_type=1,
        default_branch_id="default_branch_id_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        name="name_example",
        principal_card_id="principal_card_id_example",
    ) # PrincipalSearchQuery | principalSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of principals
        api_response = api_instance.search_principals_using_post(alias, principal_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling PrincipalsApi->search_principals_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **principal_search_query** | [**PrincipalSearchQuery**](PrincipalSearchQuery.md)| principalSearchQuery |

### Return type

[**ListResultWrapperPrincipal**](ListResultWrapperPrincipal.md)

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

# **update_principal_using_patch**
> update_principal_using_patch(alias, id, to_update)

Update principal with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import principals_api
from amparex.model.principal_to_save import PrincipalToSave
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
    api_instance = principals_api.PrincipalsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = PrincipalToSave(
        application_type=1,
        default_branch_id="default_branch_id_example",
        is_admin=False,
        last_password_change="2007-03-27T14:46:46",
        name="name_example",
        password="password_example",
        password_scheme="password_scheme_example",
        pincode="",
        pincode_hash="pincode_hash_example",
        principal_card_id="principal_card_id_example",
        staff_id="staff_id_example",
    ) # PrincipalToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update principal with given id
        api_instance.update_principal_using_patch(alias, id, to_update)
    except amparex.ApiException as e:
        print("Exception when calling PrincipalsApi->update_principal_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**PrincipalToSave**](PrincipalToSave.md)| toUpdate |

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

