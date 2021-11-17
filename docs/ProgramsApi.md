# openapi_client.ProgramsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_program_moves_using_post**](ProgramsApi.md#search_program_moves_using_post) | **POST** /alias/{alias}/protected/programmoves/search | Get a list of program moves


# **search_program_moves_using_post**
> ListResultWrapperProgramMove search_program_moves_using_post(alias, move_search_query)

Get a list of program moves

Get a list of program moves by a search query, paging is used, specify limit and page; Model Type: ProgramMove is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import programs_api
from openapi_client.model.list_result_wrapper_program_move import ListResultWrapperProgramMove
from openapi_client.model.program_move_search_query import ProgramMoveSearchQuery
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
    api_instance = programs_api.ProgramsApi(api_client)
    alias = "alias_example" # str | alias
    move_search_query = ProgramMoveSearchQuery(
        article_id="article_id_example",
        article_name_like="article_name_like_example",
        branch_id="branch_id_example",
        hours_back=1,
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
        program_name_like="program_name_like_example",
    ) # ProgramMoveSearchQuery | moveSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of program moves
        api_response = api_instance.search_program_moves_using_post(alias, move_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ProgramsApi->search_program_moves_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **move_search_query** | [**ProgramMoveSearchQuery**](ProgramMoveSearchQuery.md)| moveSearchQuery |

### Return type

[**ListResultWrapperProgramMove**](ListResultWrapperProgramMove.md)

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

