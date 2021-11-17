# SurveyTemplateSearchQuery

Search query used to filter surveytemplates

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | only fetch hidden/non-hidden templates | [optional] 
**identifier** | **str** | filter by identifier; exact match | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**only_latest** | **bool** | get only the latest version of each surveytemplate; default: true | [optional] 
**title** | **str** | filter by surveytemplate title | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


