# StaffSearchQuery

Search query used to filter staffs

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currently_employed** | **bool** | true: Only currently employed staffs are returned, false: also not employed staffs are returned | [optional] 
**employed_in_branch** | **str** | Search for staff currently employed in branch given by branch id | [optional] 
**first_name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**initials** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**surname** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


