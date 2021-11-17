# AppointmentToSave

DTO to save an appointment

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_parallel** | **bool** | Determines whether this appointment is an parallel appointment | [optional] 
**canceled** | **bool** | Determines whether this appointment is canceled | [optional] 
**comment** | **str** | Comment of the appointment | [optional] 
**customer** | [**CustomerToSave**](CustomerToSave.md) |  | [optional] 
**customer_id** | **str** | The customer for this appointment, use customer id of table customer here, nullable | [optional] 
**date** | **str** | date of the appointment - current date is used when omitted | [optional] 
**end_time** | **str** | ending time of the availability | [optional] 
**home_visit** | **bool** | Determines whether this appointment is a home visit appointment | [optional] 
**marketing_action_id** | **str** | marketing action id to create a marketing contact | [optional] 
**post_minutes** | **int** | PostMinutes of the appointment | [optional] 
**prepare_minutes** | **int** | Preparation time for the appointment | [optional] 
**resource_ids** | **str** | resourceIDs for this appointment | [optional] 
**show_as_unavailable** | **bool** | Determines whether the resource is marked as \&quot;available\&quot; for this appointment | [optional] 
**start_time** | **str** | starting time of the appointment | [optional] 
**status_id** | **str** | PredefinedPropertyID of appointment status | [optional] 
**text** | **str** | text that is to be displayed for this appointment | [optional] 
**treatment_head_id** | **str** | TreatmentHeadID of customer | [optional] 
**type_id** | **str** | PredefinedPropertyID of appointment type | [optional] 
**use_branch_id** | **str** | BranchID of the appointment - callerBranch is used when omitted | [optional] 
**whole_day** | **bool** | Determines whether the duration of the appointment is the whole day | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


