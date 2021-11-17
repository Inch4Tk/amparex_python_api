# ColorSearchQuery

Search query used to filter colors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | if true searches only for hidden colors, if false only not hidden colors are found, if empty all colors independent of hidden are found | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**only_base_color** | **bool** | true -&amp;gt; Only Base colors are searched like red, green, blue. Not producer colors like sandy beach;  false -&amp;gt; Only producer colors are searched, like sandy beach;  empty -&amp;gt; All colors are searched | [optional] 
**producer_id** | **str** | All colors related to one producer are found | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


