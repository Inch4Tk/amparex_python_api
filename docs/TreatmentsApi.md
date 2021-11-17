# openapi_client.TreatmentsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sales_order_using_post**](TreatmentsApi.md#create_sales_order_using_post) | **POST** /alias/{alias}/protected/treatments/salesorder | Create a new sales order
[**get_doctor_for_treatment_using_get**](TreatmentsApi.md#get_doctor_for_treatment_using_get) | **GET** /alias/{alias}/protected/treatments/{id}/doctors | Get the assigned doctor for the treatment
[**get_document_binary_using_get1**](TreatmentsApi.md#get_document_binary_using_get1) | **GET** /alias/{alias}/protected/treatments/{id}/documents/{did}/binary | Get document of treatment as blob
[**get_therapeutics_treatment_using_get**](TreatmentsApi.md#get_therapeutics_treatment_using_get) | **GET** /alias/{alias}/protected/treatments/therapeutics/{id} | Get one specific therapeutics treatment by id
[**get_treatment_invoices_using_get**](TreatmentsApi.md#get_treatment_invoices_using_get) | **GET** /alias/{alias}/protected/treatments/{id}/invoices | Get all documents of all types for one specific treatment
[**get_treatment_using_get**](TreatmentsApi.md#get_treatment_using_get) | **GET** /alias/{alias}/protected/treatments/{id} | Get one specific treatment by id
[**search_documents_using_post1**](TreatmentsApi.md#search_documents_using_post1) | **POST** /alias/{alias}/protected/treatments/{id}/documents/search | Get a list of treatment documents (without binary)
[**search_treatments_using_post**](TreatmentsApi.md#search_treatments_using_post) | **POST** /alias/{alias}/protected/treatments/search | Get a list of treatments


# **create_sales_order_using_post**
> TreatmentCreationResponse create_sales_order_using_post(alias, to_save)

Create a new sales order

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.sales_treatment_to_create import SalesTreatmentToCreate
from openapi_client.model.treatment_creation_response import TreatmentCreationResponse
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    to_save = SalesTreatmentToCreate(
        application_type=1,
        branch_id="branch_id_example",
        credit_card_type="credit_card_type_example",
        credit_point_number="credit_point_number_example",
        credit_point_type="credit_point_type_example",
        customer=CustomerToSave(
            address=AddressToSave(
                above_name="above_name_example",
                address_type="address_residence",
                below_name="CC Miller",
                city="Leinfelden-Echterdingen",
                comment="comment_example",
                country_code="DE",
                email="info@amparex.com",
                line1="line1_example",
                line2="line2_example",
                line3="line3_example",
                owner_id="0114ee9723da000000ea005056C00008",
                phone1="+49 (0) 711 21 475 - 475",
                phone1_sms=True,
                phone2="+49 (0) 711 21 475 - 475",
                phone2_sms=False,
                phone3="+49 (0) 711 21 475 - 475",
                phone3_sms=False,
                replace_name="replace_name_example",
                street="Max-Lang-Straße 24",
                web="www.amparex.com",
                zip="70771",
            ),
            advertising_flags=15,
            birthdate="1965-05-14",
            customer_nr_extern="customer_nr_extern_example",
            customer_since="2012-12-08",
            dominant_eye="side_right",
            dominant_hand="side_left",
            extension_name="von",
            first_name="Else",
            last_visit="2006-05-25",
            privacy_statement=True,
            privacy_statement_date="2018-05-25",
            resp_branch_id="0114ee95177000000003005056C00008",
            resp_staff_id="013a4f6d22dc00019671785d18fcca80",
            restricted_view=False,
            salutation="salutation_missis",
            status_id="013d79fd800d00000038ABCDEF364676",
            surname="Kling",
            title="Prof. Dr.",
        ),
        customer_id="customer_id_example",
        date=dateutil_parser('1970-01-01').date(),
        delivery_address=AddressToSave(
            above_name="above_name_example",
            address_type="address_residence",
            below_name="CC Miller",
            city="Leinfelden-Echterdingen",
            comment="comment_example",
            country_code="DE",
            email="info@amparex.com",
            line1="line1_example",
            line2="line2_example",
            line3="line3_example",
            owner_id="0114ee9723da000000ea005056C00008",
            phone1="+49 (0) 711 21 475 - 475",
            phone1_sms=True,
            phone2="+49 (0) 711 21 475 - 475",
            phone2_sms=False,
            phone3="+49 (0) 711 21 475 - 475",
            phone3_sms=False,
            replace_name="replace_name_example",
            street="Max-Lang-Straße 24",
            web="www.amparex.com",
            zip="70771",
        ),
        invoice_address=AddressToSave(
            above_name="above_name_example",
            address_type="address_residence",
            below_name="CC Miller",
            city="Leinfelden-Echterdingen",
            comment="comment_example",
            country_code="DE",
            email="info@amparex.com",
            line1="line1_example",
            line2="line2_example",
            line3="line3_example",
            owner_id="0114ee9723da000000ea005056C00008",
            phone1="+49 (0) 711 21 475 - 475",
            phone1_sms=True,
            phone2="+49 (0) 711 21 475 - 475",
            phone2_sms=False,
            phone3="+49 (0) 711 21 475 - 475",
            phone3_sms=False,
            replace_name="replace_name_example",
            street="Max-Lang-Straße 24",
            web="www.amparex.com",
            zip="70771",
        ),
        kind="kind_example",
        marketing_action_id="marketing_action_id_example",
        payment=3.14,
        payment_not_for_export=True,
        payment_number="payment_number_example",
        positions=[
            InvoicePositionToSave(
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
        ],
        reference_nr="reference_nr_example",
    ) # SalesTreatmentToCreate | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new sales order
        api_response = api_instance.create_sales_order_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->create_sales_order_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**SalesTreatmentToCreate**](SalesTreatmentToCreate.md)| toSave |

### Return type

[**TreatmentCreationResponse**](TreatmentCreationResponse.md)

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

# **get_doctor_for_treatment_using_get**
> Doctor get_doctor_for_treatment_using_get(alias, id)

Get the assigned doctor for the treatment

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.doctor import Doctor
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get the assigned doctor for the treatment
        api_response = api_instance.get_doctor_for_treatment_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->get_doctor_for_treatment_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Doctor**](Doctor.md)

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

# **get_document_binary_using_get1**
> str get_document_binary_using_get1(alias, id, did)

Get document of treatment as blob

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    did = "did_example" # str | did
    image_width = 1 # int | imageWidth (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get document of treatment as blob
        api_response = api_instance.get_document_binary_using_get1(alias, id, did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->get_document_binary_using_get1: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get document of treatment as blob
        api_response = api_instance.get_document_binary_using_get1(alias, id, did, image_width=image_width)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->get_document_binary_using_get1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **did** | **str**| did |
 **image_width** | **int**| imageWidth | [optional]

### Return type

**str**

### Authorization

[security_token](../README.md#security_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_therapeutics_treatment_using_get**
> TherapeuticsTreatment get_therapeutics_treatment_using_get(alias, id)

Get one specific therapeutics treatment by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.therapeutics_treatment import TherapeuticsTreatment
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific therapeutics treatment by id
        api_response = api_instance.get_therapeutics_treatment_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->get_therapeutics_treatment_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**TherapeuticsTreatment**](TherapeuticsTreatment.md)

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

# **get_treatment_invoices_using_get**
> ListResultWrapperInvoice get_treatment_invoices_using_get(alias, id)

Get all documents of all types for one specific treatment

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.list_result_wrapper_invoice import ListResultWrapperInvoice
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get all documents of all types for one specific treatment
        api_response = api_instance.get_treatment_invoices_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->get_treatment_invoices_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ListResultWrapperInvoice**](ListResultWrapperInvoice.md)

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

# **get_treatment_using_get**
> Treatment get_treatment_using_get(alias, id)

Get one specific treatment by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.treatment import Treatment
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific treatment by id
        api_response = api_instance.get_treatment_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->get_treatment_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Treatment**](Treatment.md)

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

# **search_documents_using_post1**
> ListResultWrapperDocument search_documents_using_post1(alias, id, search_query)

Get a list of treatment documents (without binary)

Get a list of treatment documents by a search query, paging is used, specify limit and page; Model Type: Documents is returned. Document is a wrapper, use id with documents/{id}/binary to get document binary itself 

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.document_search_query import DocumentSearchQuery
from openapi_client.model.list_result_wrapper_document import ListResultWrapperDocument
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    search_query = DocumentSearchQuery(
        description="description_example",
        document_source_id="document_source_id_example",
        from_date=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        mime_type="mime_type_example",
        name="name_example",
        staff_id="staff_id_example",
        to_date=dateutil_parser('Tue Dec 31 01:00:00 CET 2019').date(),
        treatment_head_id="treatment_head_id_example",
        type_id="type_id_example",
    ) # DocumentSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of treatment documents (without binary)
        api_response = api_instance.search_documents_using_post1(alias, id, search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->search_documents_using_post1: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **search_query** | [**DocumentSearchQuery**](DocumentSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperDocument**](ListResultWrapperDocument.md)

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

# **search_treatments_using_post**
> ListResultWrapperTreatment search_treatments_using_post(alias, treatment_search_query)

Get a list of treatments

Get a list of treatments by a search query, paging is used, specify limit and page; Model Type: Treatment is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import treatments_api
from openapi_client.model.treatment_search_query import TreatmentSearchQuery
from openapi_client.model.list_result_wrapper_treatment import ListResultWrapperTreatment
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
    api_instance = treatments_api.TreatmentsApi(api_client)
    alias = "alias_example" # str | alias
    treatment_search_query = TreatmentSearchQuery(
        customer_id="customer_id_example",
        end_date_from=dateutil_parser('1970-01-01').date(),
        end_date_to=dateutil_parser('1970-01-01').date(),
        kind="kind_example",
        load_complaints=True,
        load_invoices=True,
        load_refraction_reports=True,
        load_treatment_positions=True,
        load_trial_hearing_cares=True,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('1970-01-01T00:00:00.00Z'),
        modified_to=dateutil_parser('1970-01-01T00:00:00.00Z'),
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        start_date_from=dateutil_parser('1970-01-01').date(),
        start_date_to=dateutil_parser('1970-01-01').date(),
        state="state_example",
        treatment_nr="treatment_nr_example",
    ) # TreatmentSearchQuery | treatmentSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of treatments
        api_response = api_instance.search_treatments_using_post(alias, treatment_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling TreatmentsApi->search_treatments_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **treatment_search_query** | [**TreatmentSearchQuery**](TreatmentSearchQuery.md)| treatmentSearchQuery |

### Return type

[**ListResultWrapperTreatment**](ListResultWrapperTreatment.md)

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

