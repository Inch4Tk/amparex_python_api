# PrincipalSearchQuery

Search query used to filter principals

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin** | **bool** | if empty, will find all principal, also admin principal; true will find only admin principals; false will find only not admin principals | [optional] 
**application_type** | **int** | Search for principals that use the given application type | [optional] 
**default_branch_id** | **str** | Search for principals that have default branch given by branch id | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**principal_card_id** | **str** | Search for principal which has principal card given by principal card id | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


