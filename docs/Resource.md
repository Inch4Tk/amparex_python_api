# Resource

Resources are used with appointments or availabilities and describe either a staff (human resource) or a location (locale resource)

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch** | [**BranchReduced**](BranchReduced.md) |  | [optional] 
**capacity** | **int** | Specify how many appointments could be at same time, default 1 | [optional] 
**color_code** | **str** | RGB Hex color code of the resource in format #RRGGBB | [optional] 
**default_app_minutes** | **int** | Default length of an appointment of that resource in minutes | [optional] 
**description** | **str** |  | [optional] 
**for_all_branches** | **bool** | Visible for all branches | [optional] 
**for_online_booking** | **bool** | Flag if resource is anabled for online booking | [optional] 
**hidden** | **bool** | Hidden resources are set to true, not hidden false | [optional] 
**id** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Name&amp;amp;#42;\&quot; | [optional] 
**staff** | [**StaffReduced**](StaffReduced.md) |  | [optional] 
**visible_in_branches** | [**[BranchReduced]**](BranchReduced.md) | List of branches in which the resource is visible | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


