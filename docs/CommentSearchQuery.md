# CommentSearchQuery

Search query used to filter comments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_ids** | **[str]** | Shop ids, is an array of ids | [optional] 
**from_date** | **date** | comments from specified date (inclusive) | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**note** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Test&amp;amp;#42;\&quot; | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use comment/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**person_id** | **str** | Find comments of one specific person (use customerID here) | [optional] 
**staff_id** | **str** | Find comments for one specific staff | [optional] 
**to_date** | **date** | comments to specified date (inclusive) | [optional] 
**treatment_head_id** | **str** | Find comments for one specific treatment | [optional] 
**type_id** | **str** | Find comments of one specific type (PredefinedProperty id) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


