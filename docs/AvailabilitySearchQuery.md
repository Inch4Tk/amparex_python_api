# AvailabilitySearchQuery

Search query used to filter availabilities

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time** | **str** | availabilities that end before specified time (inclusive) | [optional] 
**from_date** | **date** | availabilities from specified date (inclusive) | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use availabilities/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**resource_ids** | **[str]** | availabilities using specified resources (logically and) | [optional] 
**start_time** | **str** | availabilities that start after specified time (inclusive) | [optional] 
**to_date** | **date** | availabilities to specified date (inclusive) | [optional] 
**type_ids** | **[str]** | availabilities with specified types via PredefinedPropertyID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


