# amparex.ArticleItemsApi

All URIs are relative to *http://trial.amparex.net:8078/amparex/webaxapi*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_article_item_using_get**](ArticleItemsApi.md#get_article_item_using_get) | **GET** /alias/{alias}/protected/articleitems/{id} | Get one specific articleitem by id
[**get_article_items_stock_availability_per_branch_using_get**](ArticleItemsApi.md#get_article_items_stock_availability_per_branch_using_get) | **GET** /alias/{alias}/protected/articleitems/stockavailability | Fetches stock amount per branch (shop)
[**search_article_items_using_post**](ArticleItemsApi.md#search_article_items_using_post) | **POST** /alias/{alias}/protected/articleitems/search | Get a list of articleitems
[**search_stock_amounts_using_post**](ArticleItemsApi.md#search_stock_amounts_using_post) | **POST** /alias/{alias}/protected/articleitems/stockamounts | Get a list item stock amounts
[**transfer_items_using_post**](ArticleItemsApi.md#transfer_items_using_post) | **POST** /alias/{alias}/protected/articleitems/transferitems | transfer article items from one branch to another


# **get_article_item_using_get**
> ArticleItem get_article_item_using_get(alias, id)

Get one specific articleitem by id

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import article_items_api
from amparex.model.article_item import ArticleItem
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
    api_instance = article_items_api.ArticleItemsApi(api_client)
    alias = "alias_example" # str | alias
    id = "id_example" # str | id

    # example passing only required values which don't have defaults set
    try:
        # Get one specific articleitem by id
        api_response = api_instance.get_article_item_using_get(alias, id)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ArticleItemsApi->get_article_item_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **id** | **str**| id |

### Return type

[**ArticleItem**](ArticleItem.md)

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

# **get_article_items_stock_availability_per_branch_using_get**
> [StockAvailability] get_article_items_stock_availability_per_branch_using_get(alias, articleid)

Fetches stock amount per branch (shop)

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import article_items_api
from amparex.model.stock_availability import StockAvailability
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
    api_instance = article_items_api.ArticleItemsApi(api_client)
    alias = "alias_example" # str | alias
    articleid = "articleid_example" # str | articleid

    # example passing only required values which don't have defaults set
    try:
        # Fetches stock amount per branch (shop)
        api_response = api_instance.get_article_items_stock_availability_per_branch_using_get(alias, articleid)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ArticleItemsApi->get_article_items_stock_availability_per_branch_using_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **articleid** | **str**| articleid |

### Return type

[**[StockAvailability]**](StockAvailability.md)

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

# **search_article_items_using_post**
> ListResultWrapperArticleItem search_article_items_using_post(alias, article_item_search_query)

Get a list of articleitems

Get a list of article items  by a search query, paging is used, specify limit and page; Model Type: ArticleItem is returned

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import article_items_api
from amparex.model.list_result_wrapper_article_item import ListResultWrapperArticleItem
from amparex.model.article_item_search_query import ArticleItemSearchQuery
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
    api_instance = article_items_api.ArticleItemsApi(api_client)
    alias = "alias_example" # str | alias
    article_item_search_query = ArticleItemSearchQuery(
        article_color_id="article_color_id_example",
        article_id="article_id_example",
        article_type_id="article_type_id_example",
        branch_id="branch_id_example",
        brand_id="brand_id_example",
        customer_id="0115124dc15000000003005056C00008",
        ean="ean_example",
        external_item_nr="external_item_nr_example",
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        owner=[
            "owner_example",
        ],
        producer_id="producer_id_example",
        state=[
            "state_example",
        ],
    ) # ArticleItemSearchQuery | articleItemSearchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list of articleitems
        api_response = api_instance.search_article_items_using_post(alias, article_item_search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ArticleItemsApi->search_article_items_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **article_item_search_query** | [**ArticleItemSearchQuery**](ArticleItemSearchQuery.md)| articleItemSearchQuery |

### Return type

[**ListResultWrapperArticleItem**](ListResultWrapperArticleItem.md)

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

# **search_stock_amounts_using_post**
> ListResultWrapperStockAmount search_stock_amounts_using_post(alias, search_query)

Get a list item stock amounts

Stock amount an deliverability per branch

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import article_items_api
from amparex.model.stock_amount_search_query import StockAmountSearchQuery
from amparex.model.list_result_wrapper_stock_amount import ListResultWrapperStockAmount
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
    api_instance = article_items_api.ArticleItemsApi(api_client)
    alias = "alias_example" # str | alias
    search_query = StockAmountSearchQuery(
        article_ids=[
            "article_ids_example",
        ],
        branch_ids=[
            "branch_ids_example",
        ],
        meta_data=SearchQueryMetaData(
            limit=1,
            page=1,
        ),
        variant_ids=[
            "variant_ids_example",
        ],
    ) # StockAmountSearchQuery | searchQuery

    # example passing only required values which don't have defaults set
    try:
        # Get a list item stock amounts
        api_response = api_instance.search_stock_amounts_using_post(alias, search_query)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ArticleItemsApi->search_stock_amounts_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **search_query** | [**StockAmountSearchQuery**](StockAmountSearchQuery.md)| searchQuery |

### Return type

[**ListResultWrapperStockAmount**](ListResultWrapperStockAmount.md)

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

# **transfer_items_using_post**
> CreationResponse transfer_items_using_post(alias, to_transfer)

transfer article items from one branch to another

Move items from source- to destination branch. If destination status is 'ai_state_stock' items are in stock immediately, else must be excepted by destination branch

### Example

* Api Key Authentication (security_token):

```python
import time
import amparex
from amparex.api import article_items_api
from amparex.model.creation_response import CreationResponse
from amparex.model.items_to_transfer import ItemsToTransfer
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
    api_instance = article_items_api.ArticleItemsApi(api_client)
    alias = "alias_example" # str | alias
    to_transfer = ItemsToTransfer(
        destination_branch_id="destination_branch_id_example",
        destination_status="ai_state_transfer",
        items=[
            ItemRef(
                amount=1,
                item_id="item_id_example",
            ),
        ],
        notice="Created from intranet-tool",
        source_branch_id="source_branch_id_example",
    ) # ItemsToTransfer | toTransfer

    # example passing only required values which don't have defaults set
    try:
        # transfer article items from one branch to another
        api_response = api_instance.transfer_items_using_post(alias, to_transfer)
        pprint(api_response)
    except amparex.ApiException as e:
        print("Exception when calling ArticleItemsApi->transfer_items_using_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alias** | **str**| alias |
 **to_transfer** | [**ItemsToTransfer**](ItemsToTransfer.md)| toTransfer |

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

