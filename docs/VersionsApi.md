# openapi_client.VersionsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_version_using_post**](VersionsApi.md#create_version_using_post) | **POST** /alias/{alias}/protected/versions | Create a version
[**get_latest_lts_version_using_get**](VersionsApi.md#get_latest_lts_version_using_get) | **GET** /alias/{alias}/protected/versions/LTS/latest | Get latest LTS-Version
[**get_latest_stable_lts_version_using_get**](VersionsApi.md#get_latest_stable_lts_version_using_get) | **GET** /alias/{alias}/protected/versions/LTS/latest/stable | Get latest stable LTS-Version
[**get_latest_stable_sts_version_using_get**](VersionsApi.md#get_latest_stable_sts_version_using_get) | **GET** /alias/{alias}/protected/versions/STS/latest/stable | Get latest stable STS-Version
[**get_latest_stable_version_using_get**](VersionsApi.md#get_latest_stable_version_using_get) | **GET** /alias/{alias}/protected/versions/{mainVersion}/latest/stable | Get latest stable version for given main version
[**get_latest_sts_version_using_get**](VersionsApi.md#get_latest_sts_version_using_get) | **GET** /alias/{alias}/protected/versions/STS/latest | Get latest STS-Version
[**get_latest_version_using_get**](VersionsApi.md#get_latest_version_using_get) | **GET** /alias/{alias}/protected/versions/{mainVersion}/latest | Get latest version for given main version
[**get_version_order_by_fields_using_get**](VersionsApi.md#get_version_order_by_fields_using_get) | **GET** /alias/{alias}/protected/versions/orderbyfields | Get possible fields for orderby of version fields
[**get_version_using_get**](VersionsApi.md#get_version_using_get) | **GET** /alias/{alias}/protected/versions/{id} | Get one specific version by id
[**search_versions_using_post**](VersionsApi.md#search_versions_using_post) | **POST** /alias/{alias}/protected/versions/search | Get a list of versions
[**update_version_using_patch**](VersionsApi.md#update_version_using_patch) | **PATCH** /alias/{alias}/protected/versions/{id} | Update a version


# **create_version_using_post**
> CreationResponse create_version_using_post(alias, version)

Create a version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version_to_save import VersionToSave
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias
    version = VersionToSave(
        build_time="2021-01-01 22:00:00",
        main_version="LTS-2020.4",
        main_version_id="main_version_id_example",
        number="LTS-2020.4.0.0",
        stable=True,
    ) # VersionToSave | version

    # example passing only required values which don't have defaults set
    try:
        # Create a version
        api_response = api_instance.create_version_using_post(alias, version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->create_version_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **version** | [**VersionToSave**](VersionToSave.md)| version |

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

# **get_latest_lts_version_using_get**
> Version get_latest_lts_version_using_get(alias)

Get latest LTS-Version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get latest LTS-Version
        api_response = api_instance.get_latest_lts_version_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_latest_lts_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

[**Version**](Version.md)

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

# **get_latest_stable_lts_version_using_get**
> Version get_latest_stable_lts_version_using_get(alias)

Get latest stable LTS-Version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get latest stable LTS-Version
        api_response = api_instance.get_latest_stable_lts_version_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_latest_stable_lts_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

[**Version**](Version.md)

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

# **get_latest_stable_sts_version_using_get**
> Version get_latest_stable_sts_version_using_get(alias)

Get latest stable STS-Version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get latest stable STS-Version
        api_response = api_instance.get_latest_stable_sts_version_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_latest_stable_sts_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

[**Version**](Version.md)

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

# **get_latest_stable_version_using_get**
> Version get_latest_stable_version_using_get(alias, main_version)

Get latest stable version for given main version

Main version may be either specified by name or ID

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias
    main_version = "mainVersion_example" # str | may be specified by ID, release type (such as \"LTS\") or main version (such as \"LTS-2020.4\")

    # example passing only required values which don't have defaults set
    try:
        # Get latest stable version for given main version
        api_response = api_instance.get_latest_stable_version_using_get(alias, main_version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_latest_stable_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **main_version** | **str**| may be specified by ID, release type (such as \&quot;LTS\&quot;) or main version (such as \&quot;LTS-2020.4\&quot;) |

### Return type

[**Version**](Version.md)

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

# **get_latest_sts_version_using_get**
> Version get_latest_sts_version_using_get(alias)

Get latest STS-Version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get latest STS-Version
        api_response = api_instance.get_latest_sts_version_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_latest_sts_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

[**Version**](Version.md)

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

# **get_latest_version_using_get**
> Version get_latest_version_using_get(alias, main_version)

Get latest version for given main version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias
    main_version = "mainVersion_example" # str | may be specified by ID, release type (such as \"LTS\") or main version (such as \"LTS-2020.4\")

    # example passing only required values which don't have defaults set
    try:
        # Get latest version for given main version
        api_response = api_instance.get_latest_version_using_get(alias, main_version)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_latest_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **main_version** | **str**| may be specified by ID, release type (such as \&quot;LTS\&quot;) or main version (such as \&quot;LTS-2020.4\&quot;) |

### Return type

[**Version**](Version.md)

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

# **get_version_order_by_fields_using_get**
> [str] get_version_order_by_fields_using_get(alias)

Get possible fields for orderby of version fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of version fields
        api_response = api_instance.get_version_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_version_order_by_fields_using_get: %s\n" % e)
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

# **get_version_using_get**
> Version get_version_using_get(alias, id)

Get one specific version by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version import Version
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific version by id
        api_response = api_instance.get_version_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->get_version_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Version**](Version.md)

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

# **search_versions_using_post**
> ListResultWrapperVersion search_versions_using_post(alias, version_search_query)

Get a list of versions

Get a list of versions  by a search query, paging is used, specify limit and page; Model Type: Version is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.list_result_wrapper_version import ListResultWrapperVersion
from openapi_client.model.version_search_query import VersionSearchQuery
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias
    version_search_query = VersionSearchQuery(
        build_time_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
        build_time_to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        main_version_id="main_version_id_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        number="number_example",
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        release="release_example",
        stable=False,
    ) # VersionSearchQuery | versionSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of versions
        api_response = api_instance.search_versions_using_post(alias, version_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->search_versions_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **version_search_query** | [**VersionSearchQuery**](VersionSearchQuery.md)| versionSearchQuery |

### Return type

[**ListResultWrapperVersion**](ListResultWrapperVersion.md)

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

# **update_version_using_patch**
> update_version_using_patch(alias, id, version)

Update a version

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import versions_api
from openapi_client.model.version_to_save import VersionToSave
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
    api_instance = versions_api.VersionsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    version = VersionToSave(
        build_time="2021-01-01 22:00:00",
        main_version="LTS-2020.4",
        main_version_id="main_version_id_example",
        number="LTS-2020.4.0.0",
        stable=True,
    ) # VersionToSave | version

    # example passing only required values which don't have defaults set
    try:
        # Update a version
        api_instance.update_version_using_patch(alias, id, version)
    except openapi_client.ApiException as e:
        print("Exception when calling VersionsApi->update_version_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **version** | [**VersionToSave**](VersionToSave.md)| version |

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

