# openapi_client.BrandsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_brand_image_using_get**](BrandsApi.md#get_brand_image_using_get) | **GET** /alias/{alias}/protected/brands/{brandid}/images/{imageid} | Get image of brand as blob
[**get_brand_using_get**](BrandsApi.md#get_brand_using_get) | **GET** /alias/{alias}/protected/brands/{id} | Get one specific brand by id
[**search_brands_using_post**](BrandsApi.md#search_brands_using_post) | **POST** /alias/{alias}/protected/brands/search | Get a list of brands


# **get_brand_image_using_get**
> str get_brand_image_using_get(alias, brandid, imageid)

Get image of brand as blob

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import brands_api
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
    api_instance = brands_api.BrandsApi(api_client)
    alias = "alias_example" # str | alias
    brandid = "brandid_example" # str | brandid
    imageid = "imageid_example" # str | imageid
    image_width = 1 # int | imageWidth (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get image of brand as blob
        api_response = api_instance.get_brand_image_using_get(alias, brandid, imageid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandsApi->get_brand_image_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get image of brand as blob
        api_response = api_instance.get_brand_image_using_get(alias, brandid, imageid, image_width=image_width)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandsApi->get_brand_image_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **brandid** | **str**| brandid |
 **imageid** | **str**| imageid |
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

# **get_brand_using_get**
> Brand get_brand_using_get(alias, id)

Get one specific brand by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import brands_api
from openapi_client.model.brand import Brand
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
    api_instance = brands_api.BrandsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific brand by id
        api_response = api_instance.get_brand_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandsApi->get_brand_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**Brand**](Brand.md)

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

# **search_brands_using_post**
> ListResultWrapperBrand search_brands_using_post(alias, search_query)

Get a list of brands

Get a list of brands by a search query, paging is used, specify limit and page; Model Type: Brand is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import brands_api
from openapi_client.model.list_result_wrapper_brand import ListResultWrapperBrand
from openapi_client.model.brand_search_query import BrandSearchQuery
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
    api_instance = brands_api.BrandsApi(api_client)
    alias = "alias_example" # str | alias
    search_query = BrandSearchQuery(
        application_type=1,
        for_use=True,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        name="name_example",
        producer_company_id="producer_company_id_example",
        short_name="short_name_example",
        supplier_company_id="supplier_company_id_example",
    ) # BrandSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of brands
        api_response = api_instance.search_brands_using_post(alias, search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling BrandsApi->search_brands_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**BrandSearchQuery**](BrandSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperBrand**](ListResultWrapperBrand.md)

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

