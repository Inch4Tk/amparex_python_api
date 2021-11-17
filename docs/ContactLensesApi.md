# openapi_client.ContactLensesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_contact_lense_using_post**](ContactLensesApi.md#create_contact_lense_using_post) | **POST** /alias/{alias}/protected/contactlenses | Create a new contactlense process
[**get_contact_lense_using_get**](ContactLensesApi.md#get_contact_lense_using_get) | **GET** /alias/{alias}/protected/contactlenses/{id} | Get one specific contactlense by id
[**search_contact_lenses_using_post**](ContactLensesApi.md#search_contact_lenses_using_post) | **POST** /alias/{alias}/protected/contactlenses/search | Get a list of contactlenses


# **create_contact_lense_using_post**
> CreationResponse create_contact_lense_using_post(alias, to_save)

Create a new contactlense process

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import contact_lenses_api
from openapi_client.model.contact_lense_to_save import ContactLenseToSave
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
    api_instance = contact_lenses_api.ContactLensesApi(api_client)
    alias = "alias_example" # str | alias
    to_save = ContactLenseToSave(
        connected_branch_id="0114ee9723da000000ea005056C00008",
        connected_staff_id="0114ee9723da000000ea005056C00008",
        create_invoice=Optionalboolean(
            present=True,
        ),
        customer_id="0114ee9723da000000ea005056C00008",
        invoice_positions=InvoicePositionToSave(
            amount=1.0,
            article_id="0114ee989656000001a8005056C00008",
            description="Sonderposten",
            discount=5.0,
            name="Etui",
            price=15.0,
            side="side_right, side_left",
            uid_manufacturer="1DM-OEP-REV",
            variant_id="variant_id_example",
            vat_rate=19.0,
            vat_type="vat_full",
        ),
        lense_left=ContactLenseDetail(
            addition="2.00 or high",
            amount=1.0,
            article_id="0114ee989656000001a8005056C00008",
            article_name="1 DAY ACUVUE MOIST (180er PACK)",
            axis_cylinder=75.0,
            color="Farbintensivierend Green",
            cylinder=-0.75,
            diameter=14.2,
            excentricity=2.0,
            id="id_example",
            material="Etafilcon",
            properties=OptionalMapstringstring(
                present=True,
            ),
            radius_basecurve=8.7,
            sales_price=29.9,
            sphere=2.75,
            uid_manufacturer="1DM-OEP-REV",
        ),
        lense_right=ContactLenseDetail(
            addition="2.00 or high",
            amount=1.0,
            article_id="0114ee989656000001a8005056C00008",
            article_name="1 DAY ACUVUE MOIST (180er PACK)",
            axis_cylinder=75.0,
            color="Farbintensivierend Green",
            cylinder=-0.75,
            diameter=14.2,
            excentricity=2.0,
            id="id_example",
            material="Etafilcon",
            properties=OptionalMapstringstring(
                present=True,
            ),
            radius_basecurve=8.7,
            sales_price=29.9,
            sphere=2.75,
            uid_manufacturer="1DM-OEP-REV",
        ),
        parent_treatment_head_id="0114ee9723da000000ea005056C00008",
        payed_amount=33.9,
    ) # ContactLenseToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new contactlense process
        api_response = api_instance.create_contact_lense_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactLensesApi->create_contact_lense_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**ContactLenseToSave**](ContactLenseToSave.md)| toSave |

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

# **get_contact_lense_using_get**
> ContactLense get_contact_lense_using_get(alias, id)

Get one specific contactlense by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import contact_lenses_api
from openapi_client.model.contact_lense import ContactLense
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
    api_instance = contact_lenses_api.ContactLensesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific contactlense by id
        api_response = api_instance.get_contact_lense_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactLensesApi->get_contact_lense_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ContactLense**](ContactLense.md)

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

# **search_contact_lenses_using_post**
> ListResultWrapperContactLense search_contact_lenses_using_post(alias, contactlense_search_query)

Get a list of contactlenses

Get a list of contactlenses  by a search query, paging is used, specify limit and page; Model Type: ContactLense is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import contact_lenses_api
from openapi_client.model.list_result_wrapper_contact_lense import ListResultWrapperContactLense
from openapi_client.model.contact_lense_search_query import ContactLenseSearchQuery
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
    api_instance = contact_lenses_api.ContactLensesApi(api_client)
    alias = "alias_example" # str | alias
    contactlense_search_query = ContactLenseSearchQuery(
        customer_id="customer_id_example",
        from_date=dateutil_parser('1970-01-01').date(),
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        order_number="BST-0001-20",
        to_date=dateutil_parser('1970-01-01').date(),
        treatment_id="treatment_id_example",
    ) # ContactLenseSearchQuery | contactlenseSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of contactlenses
        api_response = api_instance.search_contact_lenses_using_post(alias, contactlense_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ContactLensesApi->search_contact_lenses_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **contactlense_search_query** | [**ContactLenseSearchQuery**](ContactLenseSearchQuery.md)| contactlenseSearchQuery |

### Return type

[**ListResultWrapperContactLense**](ListResultWrapperContactLense.md)

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

