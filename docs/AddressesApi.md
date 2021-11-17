# openapi_client.AddressesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_address_using_post**](AddressesApi.md#create_address_using_post) | **POST** /alias/{alias}/protected/addresses | Create a new address
[**get_address_order_by_fields_using_get**](AddressesApi.md#get_address_order_by_fields_using_get) | **GET** /alias/{alias}/protected/addresses/orderbyfields | Get possible fields for orderby of address fields
[**get_address_using_get**](AddressesApi.md#get_address_using_get) | **GET** /alias/{alias}/protected/addresses/{id} | Get one specific address by id
[**search_addresss_using_post**](AddressesApi.md#search_addresss_using_post) | **POST** /alias/{alias}/protected/addresses/search | Get a list of addresss
[**update_address_using_patch**](AddressesApi.md#update_address_using_patch) | **PATCH** /alias/{alias}/protected/addresses/{id} | Update address with given id


# **create_address_using_post**
> CreationResponse create_address_using_post(alias, to_save)

Create a new address

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import addresses_api
from openapi_client.model.creation_response import CreationResponse
from openapi_client.model.address_to_save import AddressToSave
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
    api_instance = addresses_api.AddressesApi(api_client)
    alias = "alias_example" # str | alias
    to_save = AddressToSave(
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
    ) # AddressToSave | toSave

    # example passing only required values which don't have defaults set
    try:
        # Create a new address
        api_response = api_instance.create_address_using_post(alias, to_save)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AddressesApi->create_address_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_save** | [**AddressToSave**](AddressToSave.md)| toSave |

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

# **get_address_order_by_fields_using_get**
> [str] get_address_order_by_fields_using_get(alias)

Get possible fields for orderby of address fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import addresses_api
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
    api_instance = addresses_api.AddressesApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of address fields
        api_response = api_instance.get_address_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AddressesApi->get_address_order_by_fields_using_get: %s\n" % e)
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

# **get_address_using_get**
> Address get_address_using_get(alias, id)

Get one specific address by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import addresses_api
from openapi_client.model.address import Address
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
    api_instance = addresses_api.AddressesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific address by id
        api_response = api_instance.get_address_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AddressesApi->get_address_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Address**](Address.md)

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

# **search_addresss_using_post**
> ListResultWrapperAddress search_addresss_using_post(alias, address_search_query)

Get a list of addresss

Get a list of addresss  by a search query, paging is used, specify limit and page; Model Type: Address is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import addresses_api
from openapi_client.model.address_search_query import AddressSearchQuery
from openapi_client.model.list_result_wrapper_address import ListResultWrapperAddress
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
    api_instance = addresses_api.AddressesApi(api_client)
    alias = "alias_example" # str | alias
    address_search_query = AddressSearchQuery(
        address_type="address_type_example",
        city="city_example",
        email="email_example",
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
        owner_id="owner_id_example",
        phone1="phone1_example",
        phone2="phone2_example",
        related_type="related_type_example",
        street="street_example",
        web="web_example",
        zip="zip_example",
    ) # AddressSearchQuery | addressSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of addresss
        api_response = api_instance.search_addresss_using_post(alias, address_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling AddressesApi->search_addresss_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **address_search_query** | [**AddressSearchQuery**](AddressSearchQuery.md)| addressSearchQuery |

### Return type

[**ListResultWrapperAddress**](ListResultWrapperAddress.md)

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

# **update_address_using_patch**
> update_address_using_patch(alias, id, to_update)

Update address with given id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import addresses_api
from openapi_client.model.address_to_save import AddressToSave
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
    api_instance = addresses_api.AddressesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id
    to_update = AddressToSave(
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
    ) # AddressToSave | toUpdate

    # example passing only required values which don't have defaults set
    try:
        # Update address with given id
        api_instance.update_address_using_patch(alias, id, to_update)
    except openapi_client.ApiException as e:
        print("Exception when calling AddressesApi->update_address_using_patch: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |
 **to_update** | [**AddressToSave**](AddressToSave.md)| toUpdate |

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

