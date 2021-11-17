# SalesPriceSearchQuery

Search query used to filter sales prices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_ids** | **[str]** | a list of articles to fetch prices for | [optional] 
**branch_id** | **str** | if a branchID is given, prices are related to that branch, else prices are related to login branch | [optional] 
**changed_since** | **date** | is a date is given, (potentially) changes since then are listed | [optional] 
**for_sale** | **bool** | if true searches only for articles which are marked for sale, if false all articles which are not marked for alse are found, if empty all articles are found | [optional] 
**for_webshop** | **bool** | if true searches only for articles which are marked for webshop, if false all articles which are not marked for webshop are found, if empty all articles are found | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**start_date** | **date** | is a date is given, prices are valid at that date, else prices are valid today | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


