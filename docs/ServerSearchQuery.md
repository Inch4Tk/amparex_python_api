# ServerSearchQuery

Search query used to filter servers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**only_requested_version** | **bool** | if true searches only for requested versions, if false only not requested versions are found, if empty all servers independent of requested are found | [optional] 
**request_version** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


