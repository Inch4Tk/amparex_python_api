# Audiogram

Audiogram data in SQL useable form   The type is the kind of curve:    LAC left air conduction    RAC right air conduction      For tone audiogram the V values are the frequencies:    The intensity is the value stored in the V-fields as 0.1dB (350 = 35.0dB)    V9=12KHZ, V8=8KHz, V7=6KHz, V6=4KHz, V5=3KHZ, V4=2KHZ, V3=1KHz, V2=500Hz, V1=250Hz, V0=125Hz      Type for speech discrimination hearing loss is \"SDL\"    Values are the highest score percent in a curve of speech threshold points    V0=left un-aided   V1=right un-aided  V2=free field un-aided   V3=free field aided

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_date** | [**Timestamp**](Timestamp.md) |  | [optional] 
**customer_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**noah_action_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**v0** | **int** |  | [optional] 
**v1** | **int** |  | [optional] 
**v2** | **int** |  | [optional] 
**v3** | **int** |  | [optional] 
**v4** | **int** |  | [optional] 
**v5** | **int** |  | [optional] 
**v6** | **int** |  | [optional] 
**v7** | **int** |  | [optional] 
**v8** | **int** |  | [optional] 
**v9** | **int** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


