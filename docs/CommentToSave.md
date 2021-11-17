# CommentToSave

DTO to save a comment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**date** | **str** | Creation date of the comment, if empty current date will be used | [optional] 
**note** | **str** | The text of the comment, if empty comment will not be saved | [optional] 
**person_id** | **str** | This is the owner of the comment, use customerID here | [optional] 
**publish_branch_id** | **str** | Related branch of the comment, if empty current branch is used | [optional] 
**staff_id** | **str** | Staff which creates the comment, use id of staff here, if empty current staff will be used | [optional] 
**treatment_head_id** | **str** | Connected treatment, could be empty | [optional] 
**type_id** | **str** | Type of the comment, use id of predefined property here, if empty type note is used | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


