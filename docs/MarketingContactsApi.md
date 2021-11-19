# amparex.MarketingContactsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_marketing_contact_order_by_fields_using_get**](MarketingContactsApi.md#get_marketing_contact_order_by_fields_using_get) | **GET** /alias/{alias}/protected/marketingcontacts/orderbyfields | Get possible fields for orderby of marketingcontact fields
[**get_marketing_contact_using_get**](MarketingContactsApi.md#get_marketing_contact_using_get) | **GET** /alias/{alias}/protected/marketingcontacts/{id} | Get one specific marketingcontact by id
[**search_marketing_contacts_using_post**](MarketingContactsApi.md#search_marketing_contacts_using_post) | **POST** /alias/{alias}/protected/marketingcontacts/search | Get a list of marketingcontacts


# **get_marketing_contact_order_by_fields_using_get**
> [str] get_marketing_contact_order_by_fields_using_get(alias)

Get possible fields for orderby of marketingcontact fields

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import marketing_contacts_api
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
    api_instance = marketing_contacts_api.MarketingContactsApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of marketingcontact fields
        api_response = api_instance.get_marketing_contact_order_by_fields_using_get(alias)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling MarketingContactsApi->get_marketing_contact_order_by_fields_using_get: %s\n" % e)
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

# **get_marketing_contact_using_get**
> MarketingContact get_marketing_contact_using_get(alias, id)

Get one specific marketingcontact by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import marketing_contacts_api
from amparex.model.marketing_contact import MarketingContact
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
    api_instance = marketing_contacts_api.MarketingContactsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific marketingcontact by id
        api_response = api_instance.get_marketing_contact_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling MarketingContactsApi->get_marketing_contact_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**MarketingContact**](MarketingContact.md)

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

# **search_marketing_contacts_using_post**
> ListResultWrapperMarketingContact search_marketing_contacts_using_post(alias, marketingcontact_search_query)

Get a list of marketingcontacts

Get a list of marketingcontacts  by a search query, paging is used, specify limit and page; Model Type: MarketingContact is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import marketing_contacts_api
from amparex.model.list_result_wrapper_marketing_contact import ListResultWrapperMarketingContact
from amparex.model.marketing_contact_search_query import MarketingContactSearchQuery
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
    api_instance = marketing_contacts_api.MarketingContactsApi(api_client)
    alias = "alias_example" # str | alias
    marketingcontact_search_query = MarketingContactSearchQuery(
        created_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        created_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        marketing_action_id="marketing_action_id_example",
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
        person_id="person_id_example",
        staff_id="staff_id_example",
    ) # MarketingContactSearchQuery | marketingcontactSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of marketingcontacts
        api_response = api_instance.search_marketing_contacts_using_post(alias, marketingcontact_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling MarketingContactsApi->search_marketing_contacts_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **marketingcontact_search_query** | [**MarketingContactSearchQuery**](MarketingContactSearchQuery.md)| marketingcontactSearchQuery |

### Return type

[**ListResultWrapperMarketingContact**](ListResultWrapperMarketingContact.md)

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

