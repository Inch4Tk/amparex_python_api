# amparex.InvoicesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_invoice_using_get**](InvoicesApi.md#get_invoice_using_get) | **GET** /alias/{alias}/protected/invoice/{id} | Get one specific invoice by id
[**payment_references_using_get**](InvoicesApi.md#payment_references_using_get) | **GET** /alias/{alias}/protected/invoice/{id}/paymentreferences | Get a list of payment references for a given invoice
[**search_invoices_using_post**](InvoicesApi.md#search_invoices_using_post) | **POST** /alias/{alias}/protected/invoice/search | Get a list of invoices


# **get_invoice_using_get**
> Invoice get_invoice_using_get(alias, id)

Get one specific invoice by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import invoices_api
from amparex.model.invoice import Invoice
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
    api_instance = invoices_api.InvoicesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific invoice by id
        api_response = api_instance.get_invoice_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling InvoicesApi->get_invoice_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Invoice**](Invoice.md)

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

# **payment_references_using_get**
> {str: (str,)} payment_references_using_get(alias, id)

Get a list of payment references for a given invoice

The payment references for an invoice may depend on the country

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import invoices_api
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
    api_instance = invoices_api.InvoicesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get a list of payment references for a given invoice
        api_response = api_instance.payment_references_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling InvoicesApi->payment_references_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

**{str: (str,)}**

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

# **search_invoices_using_post**
> ListResultWrapperInvoice search_invoices_using_post(alias, invoice_search_query)

Get a list of invoices

Get a list of invoices  by a search query, paging is used, specify limit and page; Model Type: Invoice is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import invoices_api
from amparex.model.list_result_wrapper_invoice import ListResultWrapperInvoice
from amparex.model.invoice_search_query import InvoiceSearchQuery
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
    api_instance = invoices_api.InvoicesApi(api_client)
    alias = "alias_example" # str | alias
    invoice_search_query = InvoiceSearchQuery(
        customer_id="0115124dc15000000003005056C00008",
        invoice_date_from=dateutil_parser('Tue Jan 01 01:00:00 CET 2019').date(),
        invoice_date_to=dateutil_parser('Tue Dec 31 01:00:00 CET 2019').date(),
        invoice_nr="RE-*-19",
        kind="kind_glasses",
        kinds=[kind_glasses, kind_common],
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        state="invoice_state_delivered",
        treatment_id="0115124dc15000000003005056C00008",
        type="invoice_type_customer_invoice",
    ) # InvoiceSearchQuery | invoiceSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of invoices
        api_response = api_instance.search_invoices_using_post(alias, invoice_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling InvoicesApi->search_invoices_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **invoice_search_query** | [**InvoiceSearchQuery**](InvoiceSearchQuery.md)| invoiceSearchQuery |

### Return type

[**ListResultWrapperInvoice**](ListResultWrapperInvoice.md)

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

