# TreatmentSearchQuery

Search query used to filter treatments

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** |  | [optional] 
**end_date_from** | **date** |  | [optional] 
**end_date_to** | **date** |  | [optional] 
**kind** | **str** |  | [optional] 
**load_complaints** | **bool** |  | [optional] 
**load_invoices** | **bool** |  | [optional] 
**load_refraction_reports** | **bool** |  | [optional] 
**load_treatment_positions** | **bool** |  | [optional] 
**load_trial_hearing_cares** | **bool** |  | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** |  | [optional] 
**modified_to** | **datetime** |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use treatments/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**start_date_from** | **date** |  | [optional] 
**start_date_to** | **date** |  | [optional] 
**state** | **str** |  | [optional] 
**treatment_nr** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


