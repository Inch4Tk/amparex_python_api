# CompanySearchQuery

Search query, used to filter companies

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**for_use** | **bool** | if true searches only for companies which are marked for use, if false all companies which are not marked for use are found, if empty all companies are found | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches companies that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches companies that have last changed before modifiedTo (inclusive) | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**short_name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


