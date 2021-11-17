# InvoiceSearchQuery

Search query used to filter invoices

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | Searches invoices by customerID | [optional] 
**invoice_date_from** | **date** | Searches invoices by invoice date from | [optional] 
**invoice_date_to** | **date** | Searches invoices by invoice date to | [optional] 
**invoice_nr** | **str** | Searches invoices by nr | [optional] 
**kind** | **str** | Searches invoices by kind | [optional] 
**kinds** | **[str]** | Searches invoices by multiple kinds | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches invoices by last modified date from | [optional] 
**modified_to** | **datetime** | Searches invoices by last modified date to | [optional] 
**state** | **str** | Searches invoices by state | [optional] 
**treatment_id** | **str** | Searches invoices by treatment | [optional] 
**type** | **str** | Searches invoices by type | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


