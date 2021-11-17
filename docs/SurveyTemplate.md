# SurveyTemplate

customer survey template

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | [**[SurveyTemplateCategory]**](SurveyTemplateCategory.md) |  | [optional] 
**consecutive_numbering** | **bool** |  | [optional] 
**document_template_id** | **str** | id of the documenttemplate used to display this survey | [optional] 
**evaluation_formula** | **str** |  | [optional] 
**evaluation_type** | [**TranslatedString**](TranslatedString.md) |  | [optional] 
**explanation** | **str** |  | [optional] 
**groups** | [**[SurveyTemplateGroup]**](SurveyTemplateGroup.md) |  | [optional] 
**hidden** | **bool** | whether this survey is visible in the UI | [optional] 
**id** | **str** |  | [optional] 
**identifier** | **str** | survey identifier, must be identical across all versions of this survey | [optional] 
**numbering_group** | [**TranslatedString**](TranslatedString.md) |  | [optional] 
**numbering_question** | [**TranslatedString**](TranslatedString.md) |  | [optional] 
**system_name** | **str** | identifier for surveys preset by amparex | [optional] 
**take_over_answers** | **bool** | allow answers to be copied from previous survey upon creation? | [optional] 
**title** | **str** | display title | [optional] 
**type** | [**PredefinedPropertyReduced**](PredefinedPropertyReduced.md) |  | [optional] 
**version_number** | **int** | version number | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


