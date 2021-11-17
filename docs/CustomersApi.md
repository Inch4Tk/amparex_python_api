# openapi_client.CustomersApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_customer_using_post**](CustomersApi.md#create_customer_using_post) | **POST** /alias/{alias}/protected/customers | Create a new customer
[**create_document_using_post**](CustomersApi.md#create_document_using_post) | **POST** /alias/{alias}/protected/customers/{id}/documents | Create a new document for customer archive
[**get_customer_order_by_fields_using_get**](CustomersApi.md#get_customer_order_by_fields_using_get) | **GET** /alias/{alias}/protected/customers/orderbyfields | Get possible fields for orderby of customer fields
[**get_customer_using_get**](CustomersApi.md#get_customer_using_get) | **GET** /alias/{alias}/protected/customers/{id} | Get one specific customer by id
[**get_document_binary_using_get**](CustomersApi.md#get_document_binary_using_get) | **GET** /alias/{alias}/protected/customers/{cid}/documents/{did}/binary | Get document of customer as blob
[**get_document_using_get**](CustomersApi.md#get_document_using_get) | **GET** /alias/{alias}/protected/customers/{cid}/documents/{did} | Get one specfic document by id (without binary)
[**get_marketing_contacts_using_get**](CustomersApi.md#get_marketing_contacts_using_get) | **GET** /alias/{alias}/protected/customers/{id}/marketingcontacts | Get marketingcontacts for specific customer
[**search_customers_using_post**](CustomersApi.md#search_customers_using_post) | **POST** /alias/{alias}/protected/customers/search | Get a list of customers
[**search_documents_using_post**](CustomersApi.md#search_documents_using_post) | **POST** /alias/{alias}/protected/customers/{id}/documents/search | Get a list of customer documents (without binary)
[**search_documents_using_post1**](CustomersApi.md#search_documents_using_post1) | **POST** /alias/{alias}/protected/treatments/{id}/documents/search | Get a list of treatment documents (without binary)
[**update_customer_using_patch**](CustomersApi.md#update_customer_using_patch) | **PATCH** /alias/{alias}/protected/customers/{id} | Update customer with given id
[**update_document_using_patch**](CustomersApi.md#update_document_using_patch) | **PATCH** /alias/{alias}/protected/customers/{cid}/documents/{did} | Update document with given id


# **create_customer_using_post**
> CreationResponse create_customer_using_post(alias, to_save)

Create a new customer

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.creation_response import CreationResponse
from openapi_client.model.customer_to_save import CustomerToSave
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    to_save = CustomerToSave(
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
    ) # CustomerToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new customer
        api_response = api_instance.create_customer_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->create_customer_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**CustomerToSave**](CustomerToSave.md)| toSave |

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

# **create_document_using_post**
> CreationResponse create_document_using_post(alias, id, to_save)

Create a new document for customer archive

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.document_to_save import DocumentToSave
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_save = DocumentToSave(
        document_content=,
        document_description="document_description_example",
        document_name="document_name_example",
        document_source_id="document_source_id_example",
        document_template_id="document_template_id_example",
        treatment_head_id="treatment_head_id_example",
    ) # DocumentToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new document for customer archive
        api_response = api_instance.create_document_using_post(alias, id, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->create_document_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_save** | [**DocumentToSave**](DocumentToSave.md)| toSave |

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

# **get_customer_order_by_fields_using_get**
> [str] get_customer_order_by_fields_using_get(alias)

Get possible fields for orderby of customer fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of customer fields
        api_response = api_instance.get_customer_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_customer_order_by_fields_using_get: %s\n" % e)
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

# **get_customer_using_get**
> Customer get_customer_using_get(alias, id)

Get one specific customer by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.customer import Customer
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific customer by id
        api_response = api_instance.get_customer_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_customer_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Customer**](Customer.md)

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

# **get_document_binary_using_get**
> str get_document_binary_using_get(alias, cid, did)

Get document of customer as blob

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    cid = "cid_example" # str | cid
    did = "did_example" # str | did
    image_width = 1 # int | imageWidth (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get document of customer as blob
        api_response = api_instance.get_document_binary_using_get(alias, cid, did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_document_binary_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get document of customer as blob
        api_response = api_instance.get_document_binary_using_get(alias, cid, did, image_width=image_width)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_document_binary_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **cid** | **str**| cid |
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

# **get_document_using_get**
> Document get_document_using_get(alias, cid, did)

Get one specfic document by id (without binary)

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.document import Document
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    cid = "cid_example" # str | cid
    did = "did_example" # str | did

    # example passing only required values which don't have defaults set
    try:
        # Get one specfic document by id (without binary)
        api_response = api_instance.get_document_using_get(alias, cid, did)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_document_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **cid** | **str**| cid |
 **did** | **str**| did |

### Return type

[**Document**](Document.md)

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

# **get_marketing_contacts_using_get**
> ListResultWrapperMarketingContact get_marketing_contacts_using_get(alias, id)

Get marketingcontacts for specific customer

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.list_result_wrapper_marketing_contact import ListResultWrapperMarketingContact
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get marketingcontacts for specific customer
        api_response = api_instance.get_marketing_contacts_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->get_marketing_contacts_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ListResultWrapperMarketingContact**](ListResultWrapperMarketingContact.md)

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

# **search_customers_using_post**
> ListResultWrapperCustomer search_customers_using_post(alias, customer_search_query)

Get a list of customers

Get a list of customers  by a search query, paging is used, specify limit and page; Model Type: Customer is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.list_result_wrapper_customer import ListResultWrapperCustomer
from openapi_client.model.customer_search_query import CustomerSearchQuery
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    customer_search_query = CustomerSearchQuery(
        birthdate_from=dateutil_parser('Tue Mar 27 02:00:00 CEST 2018').date(),
        birthdate_to=dateutil_parser('Tue Dec 31 01:00:00 CET 2019').date(),
        branch_id="branch_id_example",
        customer_ids=[
            "customer_ids_example",
        ],
        external_customer_nr="external_customer_nr_example",
        firstname="firstname_example",
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
        status_ids=[
            "status_ids_example",
        ],
        surname="surname_example",
    ) # CustomerSearchQuery | customerSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of customers
        api_response = api_instance.search_customers_using_post(alias, customer_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->search_customers_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **customer_search_query** | [**CustomerSearchQuery**](CustomerSearchQuery.md)| customerSearchQuery |

### Return type

[**ListResultWrapperCustomer**](ListResultWrapperCustomer.md)

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

# **search_documents_using_post**
> ListResultWrapperDocument search_documents_using_post(alias, id, search_query)

Get a list of customer documents (without binary)

Get a list of customer documents  by a search query, paging is used, specify limit and page; Model Type: Documents is returned. Document is a wrapper, use id with documents/{id}/binary to get document binary itself 

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
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
        # Get a list of customer documents (without binary)
        api_response = api_instance.search_documents_using_post(alias, id, search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->search_documents_using_post: %s\n" % e)
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

# **search_documents_using_post1**
> ListResultWrapperDocument search_documents_using_post1(alias, id, search_query)

Get a list of treatment documents (without binary)

Get a list of treatment documents by a search query, paging is used, specify limit and page; Model Type: Documents is returned. Document is a wrapper, use id with documents/{id}/binary to get document binary itself 

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
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
    api_instance = customers_api.CustomersApi(api_client)
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
        print("Exception when calling CustomersApi->search_documents_using_post1: %s\n" % e)
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

# **update_customer_using_patch**
> update_customer_using_patch(alias, id, to_update)

Update customer with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.customer_to_save import CustomerToSave
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = CustomerToSave(
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
    ) # CustomerToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update customer with given id
        api_instance.update_customer_using_patch(alias, id, to_update)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->update_customer_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**CustomerToSave**](CustomerToSave.md)| toUpdate |

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

# **update_document_using_patch**
> update_document_using_patch(alias, cid, did, to_update)

Update document with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import customers_api
from openapi_client.model.document_to_save import DocumentToSave
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
    api_instance = customers_api.CustomersApi(api_client)
    alias = "alias_example" # str | alias
    cid = "cid_example" # str | cid
    did = "did_example" # str | did
    to_update = DocumentToSave(
        document_content=,
        document_description="document_description_example",
        document_name="document_name_example",
        document_source_id="document_source_id_example",
        document_template_id="document_template_id_example",
        treatment_head_id="treatment_head_id_example",
    ) # DocumentToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update document with given id
        api_instance.update_document_using_patch(alias, cid, did, to_update)
    except openapi_client.ApiException as e:
        print("Exception when calling CustomersApi->update_document_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **cid** | **str**| cid |
 **did** | **str**| did |
 **to_update** | [**DocumentToSave**](DocumentToSave.md)| toUpdate |

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
**200** | Ok - Operation successful |  -  |
**201** | Created |  -  |
**401** | Unauthorized - Check security token or credentials |  -  |
**402** | Payment Required - The API has not been activated for the company or the call-limit is exceeded |  -  |
**403** | Forbidden - Not enough permissions for this call |  -  |
**404** | NotFound - Entity not found |  -  |
**422** | Unprocessable Entity - The given entity is not valid for that request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

