# openapi_client.SurveysApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_survey_using_get**](SurveysApi.md#get_survey_using_get) | **GET** /alias/{alias}/protected/surveys/{id} | Get one specific survey by id
[**search_surveys_using_post**](SurveysApi.md#search_surveys_using_post) | **POST** /alias/{alias}/protected/surveys/search | Get a list of surveys


# **get_survey_using_get**
> Survey get_survey_using_get(alias, id)

Get one specific survey by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import surveys_api
from openapi_client.model.survey import Survey
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
    api_instance = surveys_api.SurveysApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific survey by id
        api_response = api_instance.get_survey_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveysApi->get_survey_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Survey**](Survey.md)

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

# **search_surveys_using_post**
> ListResultWrapperSurvey search_surveys_using_post(alias, survey_search_query)

Get a list of surveys

Get a list of surveys  by a search query, paging is used, specify limit and page; Model Type: Survey is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import surveys_api
from openapi_client.model.list_result_wrapper_survey import ListResultWrapperSurvey
from openapi_client.model.survey_search_query import SurveySearchQuery
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
    api_instance = surveys_api.SurveysApi(api_client)
    alias = "alias_example" # str | alias
    survey_search_query = SurveySearchQuery(
        creation_date_from=dateutil_parser('1970-01-01').date(),
        creation_date_to=dateutil_parser('1970-01-01').date(),
        customer_id="customer_id_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        state="survey_state_open, survey_state_closed",
        template_id="template_id_example",
    ) # SurveySearchQuery | surveySearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of surveys
        api_response = api_instance.search_surveys_using_post(alias, survey_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveysApi->search_surveys_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **survey_search_query** | [**SurveySearchQuery**](SurveySearchQuery.md)| surveySearchQuery |

### Return type

[**ListResultWrapperSurvey**](ListResultWrapperSurvey.md)

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

