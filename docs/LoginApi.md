# amparex.LoginApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_using_post**](LoginApi.md#change_user_using_post) | **POST** /alias/{alias}/protected/changeUser | Relogin or change user with pincode, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.
[**get_sec_token_using_post**](LoginApi.md#get_sec_token_using_post) | **POST** /alias/{alias}/login | Login with user and password, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.The use of URL parameters is a securirty isse, whenever possible use the header parameters!
[**get_sec_token_using_post1**](LoginApi.md#get_sec_token_using_post1) | **POST** /alias/{alias}/protected/axlogin | Login with AMPAREX user, password and branchId, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration. This login can be used to switch branches for a current logged-in AMPAREX user.
[**invalidate_sec_token_using_post**](LoginApi.md#invalidate_sec_token_using_post) | **POST** /alias/{alias}/protected/logout | Logout, invalidate security token
[**who_am_i_using_get**](LoginApi.md#who_am_i_using_get) | **GET** /alias/{alias}/protected/whoami | Get information about the current userlogin


# **change_user_using_post**
> SecurityToken change_user_using_post(pincode, alias)

Relogin or change user with pincode, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import login_api
from amparex.model.security_token import SecurityToken
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
    api_instance = login_api.LoginApi(api_client)
    pincode = "pincode_example" # str | pincode
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Relogin or change user with pincode, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.
        api_response = api_instance.change_user_using_post(pincode, alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LoginApi->change_user_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pincode** | **str**| pincode |
 **alias** | **str**| alias |

### Return type

[**SecurityToken**](SecurityToken.md)

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
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sec_token_using_post**
> SecurityToken get_sec_token_using_post(alias)

Login with user and password, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.The use of URL parameters is a securirty isse, whenever possible use the header parameters!

### Example


```python
import time
import amparex
from amparex.api import login_api
from amparex.model.security_token import SecurityToken
from pprint import pprint
# Defining the host is optional and defaults to http://trial.amparex.net:8078/amparex/webaxapi
# See configuration.py for a list of all supported configuration parameters.
configuration = amparex.Configuration(
    host = "http://trial.amparex.net:8078/amparex/webaxapi"
)


# Enter a context with an instance of the API client
with amparex.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = login_api.LoginApi(api_client)
    alias = "alias_example" # str | alias
    username = "username_example" # str | username (optional)
    password = "password_example" # str | password (optional)
    username2 = "username_example" # str | insecure URL parameter, better use header parameter (optional)
    password2 = "password_example" # str | insecure URL parameter, better use header parameter (optional)

    # example passing only required values which don't have defaults set
    try:
        # Login with user and password, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.The use of URL parameters is a securirty isse, whenever possible use the header parameters!
        api_response = api_instance.get_sec_token_using_post(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LoginApi->get_sec_token_using_post: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Login with user and password, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration.The use of URL parameters is a securirty isse, whenever possible use the header parameters!
        api_response = api_instance.get_sec_token_using_post(alias, username=username, password=password, username2=username2, password2=password2)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LoginApi->get_sec_token_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **username** | **str**| username | [optional]
 **password** | **str**| password | [optional]
 **username2** | **str**| insecure URL parameter, better use header parameter | [optional]
 **password2** | **str**| insecure URL parameter, better use header parameter | [optional]

### Return type

[**SecurityToken**](SecurityToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - either the username does not exists, or the given password does not match the username, or the given password does not match the security criteria (very strong) defined in AMPAREX |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |
**503** | Service Unavailable - no service configuration available that matches the specified alias |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sec_token_using_post1**
> SecurityToken get_sec_token_using_post1(username, password, branchid, alias)

Login with AMPAREX user, password and branchId, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration. This login can be used to switch branches for a current logged-in AMPAREX user.

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import login_api
from amparex.model.security_token import SecurityToken
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
    api_instance = login_api.LoginApi(api_client)
    username = "username_example" # str | username
    password = "password_example" # str | password
    branchid = "branchid_example" # str | branchid
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Login with AMPAREX user, password and branchId, use alias from AMPAREX service account. Each consecutive request, other than login, grants a new security-token with a default validity of 60 minutes. Use the new token to avoid expiration. This login can be used to switch branches for a current logged-in AMPAREX user.
        api_response = api_instance.get_sec_token_using_post1(username, password, branchid, alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LoginApi->get_sec_token_using_post1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**| username |
 **password** | **str**| password |
 **branchid** | **str**| branchid |
 **alias** | **str**| alias |

### Return type

[**SecurityToken**](SecurityToken.md)

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
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invalidate_sec_token_using_post**
> invalidate_sec_token_using_post(alias)

Logout, invalidate security token

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import login_api
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
    api_instance = login_api.LoginApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Logout, invalidate security token
        api_instance.invalidate_sec_token_using_post(alias)
    except amparex.ApiException as e:
        print("Exception when calling LoginApi->invalidate_sec_token_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

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
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **who_am_i_using_get**
> WhoAmI who_am_i_using_get(alias)

Get information about the current userlogin

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import login_api
from amparex.model.who_am_i import WhoAmI
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
    api_instance = login_api.LoginApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get information about the current userlogin
        api_response = api_instance.who_am_i_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling LoginApi->who_am_i_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |

### Return type

[**WhoAmI**](WhoAmI.md)

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

