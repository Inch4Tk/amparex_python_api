# ArticleItemSearchQuery

Search query used to filter articleitems

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_color_id** | **str** | Searches by producer color like \&quot;sandy beach\&quot;, see section color, to get id of specific color | [optional] 
**article_id** | **str** | an article to fetch items for | [optional] 
**article_type_id** | **str** | This is a predefined property ID of property type \&quot;propertytype_article_type\&quot; | [optional] 
**branch_id** | **str** | if a branchID is given, article items are related to that branch, else article items are related to login branch | [optional] 
**brand_id** | **str** | Use an id of table brand, see section brand | [optional] 
**customer_id** | **str** | Searches article items by customerID | [optional] 
**ean** | **str** | Searches by EAN/GTIN, no wildcard search | [optional] 
**external_item_nr** | **str** | Searches article items by external item Number | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**owner** | **[str]** | a list of owners to fetch items for. ai_owner_stock&#x3D; stock, ai_owner_customer &#x3D; customer, ai_owner_commission &#x3D; commission, ai_owner_deleted &#x3D; deleted, ai_owner_voucher &#x3D; voucher, ai_owner_borrow &#x3D; borrow | [optional] 
**producer_id** | **str** | Searches article items by producerID, see section company | [optional] 
**state** | **[str]** | a list of states to fetch items for. ai_state_stock &#x3D; in stock, ai_state_customer &#x3D; at the customer, ai_state_repair &#x3D; under repair, ai_state_transfer &#x3D; sent, ai_state_rejected &#x3D; rejected, ai_state_returned &#x3D; returned, ai_state_repair_intern &#x3D; internal repair, ai_state_deleted &#x3D; deleted | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


