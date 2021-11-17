# PredefinedPropertySearchQuery

Search query, used to filter predefined properties

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | if true searches only for hidden predefined properties, if false only not hidden predefined properties are found, if empty all predefined properties independent of hidden are found | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches predefined propertied that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches predefined propertied that have last changed before modifiedTo (inclusive) | [optional] 
**property_type_ids** | **[str]** | See table property type to get IDs | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


