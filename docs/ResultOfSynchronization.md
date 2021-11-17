# ResultOfSynchronization

Deliver changes in appointment planner

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**appointment** | [**AppointmentSync**](AppointmentSync.md) |  | [optional] 
**appointment_id** | **str** | Changed appointment ID | [optional] 
**entries** | [**[ResultOfSynchronization]**](ResultOfSynchronization.md) | list of changes in appointment planner | [optional] 
**removed** | **bool** | if true, appointment with given ID was deleted | [optional] 
**sync_token** | **str** | token to be sent with next synchronization request | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


