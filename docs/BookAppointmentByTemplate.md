# BookAppointmentByTemplate

Create a new appointment for given template, date and time

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | Branch information | [optional] 
**comment** | **str** | Comment for appointment, my contain customer information (name, address) as well as a user comment | [optional] 
**customer_id** | **str** | Customer for appointment | [optional] 
**date** | **date** | Date for the appointment | [optional] 
**online_booking** | **bool** | Used to filter resources in branch allowed for online booking | [optional] 
**resource_ids** | **[str]** | Explicit resources, if null resources are taken from branch and template | [optional] 
**start_time** | **str** | Start time for the appointment | [optional] 
**template_id** | **str** | Template holds information on the appointment to book | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


