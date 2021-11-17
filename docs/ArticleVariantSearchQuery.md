# ArticleVariantSearchQuery

Search query used to filter article variants

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_color_id** | **str** | Searches by producer color like \&quot;sandy beach\&quot;, see section color, to get id of specific color | [optional] 
**article_id** | **str** | an article to fetch items for | [optional] 
**delivery_state** | **[str]** | a list of delivery states to fetch article variants for. article_variant_delivery_state_yes &#x3D; Deliverable, article_variant_delivery_state_no &#x3D; Not deliverable, article_variant_delivery_state_temporarily_not &#x3D; Temporarily not deliverable | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**prefered_order_owner_type** | **[str]** | a list of owners to fetch article variants for. order_type_firm&#x3D; stock, order_owner_type_with_return &#x3D; Stock (for credit), order_type_commission &#x3D; commission, order_owner_type_borrow &#x3D; borrow | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


