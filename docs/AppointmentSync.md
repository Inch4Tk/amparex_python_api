# AppointmentSync

Detailed information about one appointment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** |  | [optional] 
**canceled** | **bool** | Indicates whether an appointment has been cancelled | [optional] 
**comment** | **str** |  | [optional] 
**creation** | **datetime** | The technical creation date for this appointment | [optional] 
**customer** | [**CustomerReducedWithEmail**](CustomerReducedWithEmail.md) |  | [optional] 
**date** | **date** |  | [optional] 
**end_time** | **str** |  | [optional] 
**home_visit** | **bool** | Indicates whether an appointment is marked as homeVisit | [optional] 
**id** | **str** |  | [optional] 
**is_availability** | **bool** | Is availabilty (or appointment) | [optional] 
**last_notification** | **datetime** | Last notification to customer | [optional] 
**post_minutes** | **int** | The post preparation time for this appointment | [optional] 
**prepare_minutes** | **int** | The preparation time for this appointment | [optional] 
**resources** | [**[ResourceReduced]**](ResourceReduced.md) | A list of resources for this appointment | [optional] 
**show_as_unavailable** | **bool** | Is un-available | [optional] 
**start_time** | **str** |  | [optional] 
**status** | [**PredefinedPropertySimple**](PredefinedPropertySimple.md) |  | [optional] 
**text** | **str** |  | [optional] 
**treatment_id** | **str** |  | [optional] 
**type** | [**PredefinedPropertySimple**](PredefinedPropertySimple.md) |  | [optional] 
**whole_day** | **bool** | Indicates whether an appointment is sheduled for the whole day | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


