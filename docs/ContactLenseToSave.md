# ContactLenseToSave

DTO to save a contactlense

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected_branch_id** | **str** | The ID of the branch that has sold the contact lense | [optional] 
**connected_staff_id** | **str** | The ID of the staff that has sold the contact lense | [optional] 
**create_invoice** | [**Optionalboolean**](Optionalboolean.md) |  | [optional] 
**customer_id** | **str** | The customerID this lense belongs to. A new process will be created | [optional] 
**invoice_positions** | [**InvoicePositionToSave**](InvoicePositionToSave.md) |  | [optional] 
**lense_left** | [**ContactLenseDetail**](ContactLenseDetail.md) |  | [optional] 
**lense_right** | [**ContactLenseDetail**](ContactLenseDetail.md) |  | [optional] 
**parent_treatment_head_id** | **str** | The ID of an allready existing process. The new lense will be created as a follow up lense for the existing process | [optional] 
**payed_amount** | **float** | The amount that has already been payed along with this sale | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


