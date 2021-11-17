# AppointmentFreeBusySearchQuery

Search free/busy time slots for appointments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branch_id** | **str** | branch to find slots for | [optional] 
**duration_minutes** | **int** | find availabilities with given minimum duration only | [optional] 
**end_date** | **date** | end date for search, default equals to start | [optional] 
**end_time** | **str** | generate slots until at given time per day | [optional] 
**free_slots_only** | **bool** | if true busy slots are not sent (only free-slots) | [optional] 
**online_booking** | **bool** | find slots for online booking | [optional] 
**resource_ids** | **[str]** | if not null, this resource is requested for free/busy slots | [optional] 
**slice_free_slots** | **bool** | deliver free slots in pieces of bookable entries | [optional] 
**start_date** | **date** | start date for search, default today | [optional] 
**start_time** | **str** | generate slots staring at given time per day | [optional] 
**step_minutes** | **int** | generate slots with multiples of given step size | [optional] 
**template_id** | **str** | appointment template to search slots for | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


