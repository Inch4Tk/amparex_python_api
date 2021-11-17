# ArticleSearchQuery

Search query used to filter articles

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_properties** | [**ArticlePropertiesMeta**](ArticlePropertiesMeta.md) |  | [optional] 
**article_type_id** | **str** | This is a predefined property ID of property type \&quot;propertytype_article_type\&quot; | [optional] 
**base_color_id** | **str** | Search for base color like \&quot;white\&quot;, see section color, to get id of specific color | [optional] 
**brand_id** | **str** | Use a id of table brand, see section brand | [optional] 
**changed_since** | **date** | is a date is given, (potentially) changes since then are listed | [optional] 
**color_id** | **str** | Search for producer color like \&quot;sandy beach\&quot;, see section color, to get id of specific color | [optional] 
**ean** | **str** | Search for EAN/GTIN, no wildcard search | [optional] 
**for_sale** | **bool** | if true searches only for articles which are marked for sale, if false all articles which are not marked for alse are found, if empty all articles are found | [optional] 
**for_use** | **bool** | if true searches only for articles which are marked for use, if false all articles which are not marked for use are found, if empty all articles are found | [optional] 
**for_webshop** | **bool** | if true searches only for articles which are marked for webshop, if false all articles which are not marked for webshop are found, if empty all articles are found | [optional] 
**generic_search** | **str** | Generic search field, which searches in multiple data (article name, brand and color). Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**group_by_name_and_brand** | **bool** | Group together frames by model and brand, use link to similar article to get different articles in the group | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches articles that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches articles that have last changed before modifiedTo (inclusive) | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use article/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**producer_company_id** | **str** | Use a id of table company, see section company | [optional] 
**without_locked** | **bool** | if true searches only for articles which are not locked,  if empty or false all articles are found | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


