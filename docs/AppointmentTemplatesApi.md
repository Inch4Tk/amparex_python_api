# amparex.AppointmentTemplatesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_appointment_templates_using_post**](AppointmentTemplatesApi.md#search_appointment_templates_using_post) | **POST** /alias/{alias}/protected/appointmenttemplates/search | Get a list of appointment templates


# **search_appointment_templates_using_post**
> ListResultWrapperAppointmentTemplate search_appointment_templates_using_post(alias, search_query)

Get a list of appointment templates

Get a list of templates for online booking by branch-id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import appointment_templates_api
from amparex.model.list_result_wrapper_appointment_template import ListResultWrapperAppointmentTemplate
from amparex.model.appointment_template_search_query import AppointmentTemplateSearchQuery
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
    api_instance = appointment_templates_api.AppointmentTemplatesApi(api_client)
    alias = "alias_example" # str | alias
    search_query = AppointmentTemplateSearchQuery(
        branch_id="branch_id_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        online_booking=False,
    ) # AppointmentTemplateSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of appointment templates
        api_response = api_instance.search_appointment_templates_using_post(alias, search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling AppointmentTemplatesApi->search_appointment_templates_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**AppointmentTemplateSearchQuery**](AppointmentTemplateSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperAppointmentTemplate**](ListResultWrapperAppointmentTemplate.md)

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

