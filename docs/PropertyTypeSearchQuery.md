# PropertyTypeSearchQuery

Search query, used to filter property types

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **[str]** | All categories are available with url ../properties/propertytypes/categories | [optional] 
**hidden** | **bool** | if true searches only for hidden property types, if false only not hidden property types are found, if empty all property types independent of hidden are found | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches property types that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches property types that have last changed before modifiedTo (inclusive) | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


