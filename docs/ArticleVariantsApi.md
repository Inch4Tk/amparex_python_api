# openapi_client.ArticleVariantsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_variant_using_get**](ArticleVariantsApi.md#get_article_variant_using_get) | **GET** /alias/{alias}/protected/articlevariants/{id} | Get one specific article variant by id
[**search_article_variants_using_post**](ArticleVariantsApi.md#search_article_variants_using_post) | **POST** /alias/{alias}/protected/articlevariants/search | Get a list of article variants


# **get_article_variant_using_get**
> ArticleVariant get_article_variant_using_get(alias, id)

Get one specific article variant by id

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import article_variants_api
from openapi_client.model.article_variant import ArticleVariant
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
    api_instance = article_variants_api.ArticleVariantsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific article variant by id
        api_response = api_instance.get_article_variant_using_get(alias, id)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticleVariantsApi->get_article_variant_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ArticleVariant**](ArticleVariant.md)

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

# **search_article_variants_using_post**
> ListResultWrapperArticleVariant search_article_variants_using_post(alias, articlevariant_search_query)

Get a list of article variants

Get a list of article variants  by a search query, paging is used, specify limit and page; Model Type: ArticleVariant is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import openapi_client
from openapi_client.api import article_variants_api
from openapi_client.model.list_result_wrapper_article_variant import ListResultWrapperArticleVariant
from openapi_client.model.article_variant_search_query import ArticleVariantSearchQuery
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
    api_instance = article_variants_api.ArticleVariantsApi(api_client)
    alias = "alias_example" # str | alias
    articlevariant_search_query = ArticleVariantSearchQuery(
        article_color_id="article_color_id_example",
        article_id="article_id_example",
        delivery_state=[
            "delivery_state_example",
        ],
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        prefered_order_owner_type=[
            "prefered_order_owner_type_example",
        ],
    ) # ArticleVariantSearchQuery | articlevariantSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of article variants
        api_response = api_instance.search_article_variants_using_post(alias, articlevariant_search_query)
        pprint(api_response)
    except openapi_client.ApiException as e:
        print("Exception when calling ArticleVariantsApi->search_article_variants_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **articlevariant_search_query** | [**ArticleVariantSearchQuery**](ArticleVariantSearchQuery.md)| articlevariantSearchQuery |

### Return type

[**ListResultWrapperArticleVariant**](ListResultWrapperArticleVariant.md)

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

