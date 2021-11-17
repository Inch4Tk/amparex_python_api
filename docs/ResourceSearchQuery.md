# ResourceSearchQuery

Search query used to filter resources

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | resources for specified branchID | [optional] 
**for_online_booking** | **bool** | if true, only resources enabled for online booking are found | [optional] 
**hidden** | **bool** | if empty, will find all resources, also hidden; true will find only hidden resources; false will find only not hidden resources | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches resources that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches resources that have last changed before modifiedTo (inclusive) | [optional] 
**name** | **str** | resources with specified name | [optional] 
**staff_id** | **str** | resources for specified staffID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


