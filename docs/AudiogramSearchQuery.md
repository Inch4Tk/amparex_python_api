# AudiogramSearchQuery

Search query used to filter audiograms

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date_from** | **date** | audiograms from specified date (inclusive) | [optional] 
**create_date_until** | **date** | audiograms from specified date (inclusive) | [optional] 
**customer_id** | **str** |  | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches audiograms that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches audiograms that have last changed before modifiedTo (inclusive) | [optional] 
**noah_action_id** | **str** |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use doctor/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**type** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


