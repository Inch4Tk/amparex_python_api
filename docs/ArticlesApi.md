# openapi_client.ArticlesApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_image_using_get**](ArticlesApi.md#get_article_image_using_get) | **GET** /alias/{alias}/protected/articles/{articleid}/images/{imageid} | Get image of article as blob
[**get_article_order_by_fields_using_get**](ArticlesApi.md#get_article_order_by_fields_using_get) | **GET** /alias/{alias}/protected/articles/orderbyfields | Get possible fields for orderby of article fields
[**get_article_using_get**](ArticlesApi.md#get_article_using_get) | **GET** /alias/{alias}/protected/articles/{id} | Get one specific article detail by id
[**search_articles_using_post**](ArticlesApi.md#search_articles_using_post) | **POST** /alias/{alias}/protected/articles/search | Get a list of articles
[**search_detailed_articles_using_post**](ArticlesApi.md#search_detailed_articles_using_post) | **POST** /alias/{alias}/protected/articles/detailedsearch | Get a list of detailed articles
[**search_sales_prices_using_post**](ArticlesApi.md#search_sales_prices_using_post) | **POST** /alias/{alias}/protected/articles/salesprices/search | Get a list of article sales prices


# **get_article_image_using_get**
> str get_article_image_using_get(alias, articleid, imageid)

Get image of article as blob

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import articles_api
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
    api_instance = articles_api.ArticlesApi(api_client)
    alias = "alias_example" # str | alias
    articleid = "articleid_example" # str | articleid
    imageid = "imageid_example" # str | imageid
    image_width = 1 # int | imageWidth (optional)

    # example passing only required values which don't have defaults set
    try:
        # Get image of article as blob
        api_response = api_instance.get_article_image_using_get(alias, articleid, imageid)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->get_article_image_using_get: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Get image of article as blob
        api_response = api_instance.get_article_image_using_get(alias, articleid, imageid, image_width=image_width)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->get_article_image_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **articleid** | **str**| articleid |
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

# **get_article_order_by_fields_using_get**
> [str] get_article_order_by_fields_using_get(alias)

Get possible fields for orderby of article fields

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import articles_api
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
    api_instance = articles_api.ArticlesApi(api_client)
    alias = "alias_example" # str | alias

    # example passing only required values which don't have defaults set
    try:
        # Get possible fields for orderby of article fields
        api_response = api_instance.get_article_order_by_fields_using_get(alias)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->get_article_order_by_fields_using_get: %s\n" % e)
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

# **get_article_using_get**
> ArticleDetail get_article_using_get(alias, id)

Get one specific article detail by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import articles_api
from openapi_client.model.article_detail import ArticleDetail
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
    api_instance = articles_api.ArticlesApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific article detail by id
        api_response = api_instance.get_article_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->get_article_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ArticleDetail**](ArticleDetail.md)

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

# **search_articles_using_post**
> ListResultWrapperArticleOverview search_articles_using_post(alias, article_search_query)

Get a list of articles

Get a list of articles  by a search query, paging is used, specify limit and page; Model Type: ArticleOverview is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import articles_api
from openapi_client.model.list_result_wrapper_article_overview import ListResultWrapperArticleOverview
from openapi_client.model.article_search_query import ArticleSearchQuery
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
    api_instance = articles_api.ArticlesApi(api_client)
    alias = "alias_example" # str | alias
    article_search_query = ArticleSearchQuery(
        article_properties=ArticlePropertiesMeta(
            operator="operator_example",
            properties=[
                SearchPropertyEntry(
                    predefined_property_id="predefined_property_id_example",
                    property_type_id="property_type_id_example",
                ),
            ],
        ),
        article_type_id="article_type_id_example",
        base_color_id="base_color_id_example",
        brand_id="brand_id_example",
        changed_since=dateutil_parser('Fri Jan 01 01:00:00 CET 2021').date(),
        color_id="color_id_example",
        ean="ean_example",
        for_sale=True,
        for_use=True,
        for_webshop=False,
        generic_search="generic_search_example",
        group_by_name_and_brand=False,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        name="name_example",
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        producer_company_id="producer_company_id_example",
        without_locked=True,
    ) # ArticleSearchQuery | articleSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of articles
        api_response = api_instance.search_articles_using_post(alias, article_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->search_articles_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **article_search_query** | [**ArticleSearchQuery**](ArticleSearchQuery.md)| articleSearchQuery |

### Return type

[**ListResultWrapperArticleOverview**](ListResultWrapperArticleOverview.md)

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

# **search_detailed_articles_using_post**
> ListResultWrapperArticleDetail search_detailed_articles_using_post(alias, article_search_query)

Get a list of detailed articles

Get a list of detailed articles  by a search query, contains more details than /search including properties &amp; images, paging is used, specify limit and page; Model Type: ArticleDetail is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import articles_api
from openapi_client.model.list_result_wrapper_article_detail import ListResultWrapperArticleDetail
from openapi_client.model.article_search_query import ArticleSearchQuery
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
    api_instance = articles_api.ArticlesApi(api_client)
    alias = "alias_example" # str | alias
    article_search_query = ArticleSearchQuery(
        article_properties=ArticlePropertiesMeta(
            operator="operator_example",
            properties=[
                SearchPropertyEntry(
                    predefined_property_id="predefined_property_id_example",
                    property_type_id="property_type_id_example",
                ),
            ],
        ),
        article_type_id="article_type_id_example",
        base_color_id="base_color_id_example",
        brand_id="brand_id_example",
        changed_since=dateutil_parser('Fri Jan 01 01:00:00 CET 2021').date(),
        color_id="color_id_example",
        ean="ean_example",
        for_sale=True,
        for_use=True,
        for_webshop=False,
        generic_search="generic_search_example",
        group_by_name_and_brand=False,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        modified_from=dateutil_parser('2019-11-05T06:35:00+01:00'),
        modified_to=dateutil_parser('2019-11-05T06:35:00+01:00'),
        name="name_example",
        order_by=[
            OrderBy(
                asc_desc="asc_desc_example",
                field_name="field_name_example",
            ),
        ],
        producer_company_id="producer_company_id_example",
        without_locked=True,
    ) # ArticleSearchQuery | articleSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of detailed articles
        api_response = api_instance.search_detailed_articles_using_post(alias, article_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->search_detailed_articles_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **article_search_query** | [**ArticleSearchQuery**](ArticleSearchQuery.md)| articleSearchQuery |

### Return type

[**ListResultWrapperArticleDetail**](ListResultWrapperArticleDetail.md)

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

# **search_sales_prices_using_post**
> ListResultWrapperSalesPrice search_sales_prices_using_post(alias, search_query)

Get a list of article sales prices

Get a list of sales prices by a search query, paging is used, specify limit and page; Model Type: SalesPrice is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import articles_api
from openapi_client.model.list_result_wrapper_sales_price import ListResultWrapperSalesPrice
from openapi_client.model.sales_price_search_query import SalesPriceSearchQuery
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
    api_instance = articles_api.ArticlesApi(api_client)
    alias = "alias_example" # str | alias
    search_query = SalesPriceSearchQuery(
        article_ids=[
            "article_ids_example",
        ],
        branch_id="branch_id_example",
        changed_since=dateutil_parser('Fri Jan 01 01:00:00 CET 2021').date(),
        for_sale=True,
        for_webshop=False,
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        start_date=dateutil_parser('Fri Jan 01 01:00:00 CET 2021').date(),
    ) # SalesPriceSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of article sales prices
        api_response = api_instance.search_sales_prices_using_post(alias, search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticlesApi->search_sales_prices_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**SalesPriceSearchQuery**](SalesPriceSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperSalesPrice**](ListResultWrapperSalesPrice.md)

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

