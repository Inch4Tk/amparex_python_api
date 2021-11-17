# BranchSearchQuery

Search query used to filter branch

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_at** | **date** | If date is set, returns only active branches at that date, if date is not set, also inactive branches are returned | [optional] 
**application_type** | **int** | If not Null, return only branches fitting at least on application type are returned | [optional] 
**is_treating** | **bool** | If true only treating branches are returned, if false only non-treating branches are returned | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches branches that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches branches that have last changed before modifiedTo (inclusive) | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


