# ViewToSave

DTO to save a view

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | Connected to table branch, nullable | [optional] 
**connected_resources** | [**[ViewResourceToSave]**](ViewResourceToSave.md) | List of connectedResources, which are assigned to the view | [optional] 
**days** | **int** | Count in days which are visible by default, if empty 1 or 5 is set depending on type of view | [optional] 
**end_time** | **str** | End time to which default view is visible, if not set default is 18:00:00 | [optional] 
**name** | **str** | Name of the view, not null | [optional] 
**ruler_minutes** | **int** | Grid size of the timeplanner in minutes, default is 60 | [optional] 
**sorting** | **int** | Sequence of tab order, beginning with smallest, default is 10 | [optional] 
**start_time** | **str** | Start time from which default view is visible, if not set default is 09:00:00 | [optional] 
**text** | **str** | Text in the header title, nullable | [optional] 
**title** | **str** | Text of the timeplanner tab, not null | [optional] 
**type** | **str** | Not null, Use one of the following values: resource_planner, day_planner, treatment_planner | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


