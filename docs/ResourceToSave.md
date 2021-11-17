# ResourceToSave

DTO to save a resource

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | Use branch id of table branch here, used for location resource. Maybe null if human resource | [optional] 
**capacity** | **int** | Specify how many appointments could be at same time, default 1 | [optional] 
**color_code** | **str** | Specify color in format Hex format #RRGGBB, e.g. #01FFAE, default is black | [optional] 
**default_app_minutes** | **int** | Specify default length of appointment, 60 minutes if not given | [optional] 
**description** | **str** | Describes the resoruce, nullable | [optional] 
**for_all_branches** | **bool** | Visible for all branches, default is false | [optional] 
**hidden** | **bool** | To hide a resource set hidden to true, default false | [optional] 
**name** | **str** | Name of the resource, not null | [optional] 
**staff_id** | **str** | Use staff id of table staff here, used for human resource. Maybe null if location resource | [optional] 
**visible_in_branches** | **[str]** | List of branch ids in which the resource is visible | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


