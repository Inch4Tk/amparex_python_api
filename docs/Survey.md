# Survey

customer survey

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**answers** | [**[SurveyAnswer]**](SurveyAnswer.md) |  | [optional] 
**creation_date** | **datetime** | date the survey was first started for this customer | [optional] 
**customer** | [**CustomerReduced**](CustomerReduced.md) |  | [optional] 
**id** | **str** |  | [optional] 
**result** | **str** | if the survey was evaluated based on a formula, this is the result of that evaluation | [optional] 
**staff** | [**StaffReduced**](StaffReduced.md) |  | [optional] 
**state** | [**TranslatedString**](TranslatedString.md) |  | [optional] 
**sum_weighting** | **int** | if weighting was done, this is the weighted result of all answers | [optional] 
**survey_template_id** | **str** |  | [optional] 
**treatment_position_id** | **str** | if this survey was done as part of a treatment process, this id refers to the step in the treatment | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


