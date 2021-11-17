# AppointmentSearchQuery

Search query used to filter appointments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | appointments for specified branchID | [optional] 
**customer_id** | **str** | appointments for specified customerID | [optional] 
**end_time** | **str** | appointments that end before specified time (inclusive) | [optional] 
**from_date** | **date** | appointments from specified date (inclusive) | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches appointments that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches appointments that have last changed before modifiedTo (inclusive) | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use appointment/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**resource_ids** | **[str]** | appointments using specified resources (logically and) | [optional] 
**start_time** | **str** | appointments that start after specified time (inclusive) | [optional] 
**status_id** | **str** | appointments with specified status via PredefinedPropertyID | [optional] 
**to_date** | **date** | appointments to specified date (inclusive) | [optional] 
**treatment_id** | **str** | appointments for specified treatment | [optional] 
**type_id** | **str** | appointments with specified type via PredefinedPropertyID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


