# DeliverySearchQuery

Search query used to filter deliveries

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delivery_nr** | **str** | Searches by delivery note number | [optional] 
**delivery_type** | **str** | Searches by delivery type. Use one of the following values : delivery_type_storage, delivery_type_restorage_repair, delivery_type_internal_transfer, delivery_type_return, delivery_type_return_comission, delivery_type_return_repair, delivery_type_return_voucher, delivery_type_handout, delivery_type_handout_borrow, delivery_type_handout_repair, delivery_type_drop_shipment, delivery_type_marketplace | [optional] 
**from_delivery_date** | **date** | Searches deliveries that delivered after fromDeliveryDate (inclusive) | [optional] 
**from_delivery_note_date** | **date** | Searches deliveries that have delivery note date after fromDeliveryNoteDate (inclusive) | [optional] 
**from_person_id** | **str** | Searches by sender id | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use delivery/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**to_delivery_date** | **date** | Searches deliveries that delivered before toDeliveryDate (inclusive) | [optional] 
**to_delivery_note_date** | **date** | Searches deliveries that have delivery note date before fromDeliveryNoteDate (inclusive) | [optional] 
**to_person_id** | **str** | Searches by receiver id | [optional] 
**tracking_number** | **str** | Searches by tracking number | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


