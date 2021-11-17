# openapi_client.SurveyTemplatesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_survey_template_using_post**](SurveyTemplatesApi.md#create_survey_template_using_post) | **POST** /alias/{alias}/protected/surveytemplates | Create a new surveytemplate
[**delete_survey_template_using_delete**](SurveyTemplatesApi.md#delete_survey_template_using_delete) | **DELETE** /alias/{alias}/protected/surveytemplates/{id} | Delete a surveytemplate with given id
[**get_survey_template_using_get**](SurveyTemplatesApi.md#get_survey_template_using_get) | **GET** /alias/{alias}/protected/surveytemplates/{id} | Get one specific surveytemplate by id
[**search_survey_templates_using_post**](SurveyTemplatesApi.md#search_survey_templates_using_post) | **POST** /alias/{alias}/protected/surveytemplates/search | Get a list of surveytemplates
[**update_survey_template_using_patch**](SurveyTemplatesApi.md#update_survey_template_using_patch) | **PATCH** /alias/{alias}/protected/surveytemplates/{id} | Update surveytemplate with given id


# **create_survey_template_using_post**
> CreationResponse create_survey_template_using_post(alias, to_save)

Create a new surveytemplate

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import survey_templates_api
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
    api_instance = survey_templates_api.SurveyTemplatesApi(api_client)
    alias = "alias_example" # str | alias
    to_save = {} # bool, date, datetime, dict, float, int, list, str, none_type | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new surveytemplate
        api_response = api_instance.create_survey_template_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveyTemplatesApi->create_survey_template_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | **bool, date, datetime, dict, float, int, list, str, none_type**| toSave |

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

# **delete_survey_template_using_delete**
> delete_survey_template_using_delete(alias, id)

Delete a surveytemplate with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import survey_templates_api
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
    api_instance = survey_templates_api.SurveyTemplatesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Delete a surveytemplate with given id
        api_instance.delete_survey_template_using_delete(alias, id)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveyTemplatesApi->delete_survey_template_using_delete: %s\n" % e)
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

# **get_survey_template_using_get**
> SurveyTemplate get_survey_template_using_get(alias, id)

Get one specific surveytemplate by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import survey_templates_api
from openapi_client.model.survey_template import SurveyTemplate
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
    api_instance = survey_templates_api.SurveyTemplatesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific surveytemplate by id
        api_response = api_instance.get_survey_template_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveyTemplatesApi->get_survey_template_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**SurveyTemplate**](SurveyTemplate.md)

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

# **search_survey_templates_using_post**
> ListResultWrapperSurveyTemplate search_survey_templates_using_post(alias, surveytemplate_search_query)

Get a list of surveytemplates

Get a list of surveytemplates  by a search query, paging is used, specify limit and page; Model Type: SurveyTemplate is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import survey_templates_api
from openapi_client.model.survey_template_search_query import SurveyTemplateSearchQuery
from openapi_client.model.list_result_wrapper_survey_template import ListResultWrapperSurveyTemplate
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
    api_instance = survey_templates_api.SurveyTemplatesApi(api_client)
    alias = "alias_example" # str | alias
    surveytemplate_search_query = SurveyTemplateSearchQuery(
        hidden=False,
        identifier="identifier_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        only_latest=False,
        title="title_example",
    ) # SurveyTemplateSearchQuery | surveytemplateSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of surveytemplates
        api_response = api_instance.search_survey_templates_using_post(alias, surveytemplate_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveyTemplatesApi->search_survey_templates_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **surveytemplate_search_query** | [**SurveyTemplateSearchQuery**](SurveyTemplateSearchQuery.md)| surveytemplateSearchQuery |

### Return type

[**ListResultWrapperSurveyTemplate**](ListResultWrapperSurveyTemplate.md)

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

# **update_survey_template_using_patch**
> update_survey_template_using_patch(alias, id, to_update)

Update surveytemplate with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import survey_templates_api
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
    api_instance = survey_templates_api.SurveyTemplatesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = {} # bool, date, datetime, dict, float, int, list, str, none_type | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update surveytemplate with given id
        api_instance.update_survey_template_using_patch(alias, id, to_update)
    except openapi_client.ApiException as e:
        print("Exception when calling SurveyTemplatesApi->update_survey_template_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | **bool, date, datetime, dict, float, int, list, str, none_type**| toUpdate |

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

