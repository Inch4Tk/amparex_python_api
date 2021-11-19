# amparex.ServersApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_server_using_get**](ServersApi.md#get_server_using_get) | **GET** /alias/{alias}/protected/servers/{id} | Get one specific server by id
[**search_servers_using_post**](ServersApi.md#search_servers_using_post) | **POST** /alias/{alias}/protected/servers/search | Get a list of servers


# **get_server_using_get**
> Server get_server_using_get(alias, id)

Get one specific server by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import servers_api
from amparex.model.server import Server
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
    api_instance = servers_api.ServersApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific server by id
        api_response = api_instance.get_server_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ServersApi->get_server_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Server**](Server.md)

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

# **search_servers_using_post**
> ListResultWrapperServer search_servers_using_post(alias, server_search_query)

Get a list of servers

Get a list of servers  by a search query, paging is used, specify limit and page; Model Type: Server is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import servers_api
from amparex.model.server_search_query import ServerSearchQuery
from amparex.model.list_result_wrapper_server import ListResultWrapperServer
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
    api_instance = servers_api.ServersApi(api_client)
    alias = "alias_example" # str | alias
    server_search_query = ServerSearchQuery(
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        name="name_example",
        only_requested_version=False,
        request_version="request_version_example",
    ) # ServerSearchQuery | serverSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of servers
        api_response = api_instance.search_servers_using_post(alias, server_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ServersApi->search_servers_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **server_search_query** | [**ServerSearchQuery**](ServerSearchQuery.md)| serverSearchQuery |

### Return type

[**ListResultWrapperServer**](ListResultWrapperServer.md)

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

