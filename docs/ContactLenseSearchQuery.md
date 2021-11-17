# ContactLenseSearchQuery

Search query used to filter contactlenses

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | contact lenses for specified customerID | [optional] 
**from_date** | **date** | contact lenses created after a specified from date | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches contact lenses that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches contact lenses that have last changed before modifiedTo (inclusive) | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use customer/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**order_number** | **str** | Searches contact lenses that have been ordered with a given AMPAREX order number | [optional] 
**to_date** | **date** | contact lenses created before a specified to date | [optional] 
**treatment_id** | **str** | contact lenses for specified treatmentID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


