# InvoicePositionToSave

Object to store invoice positions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount | [optional] 
**article_id** | **str** | The ID of the article | [optional] 
**description** | **str** | Additional description | [optional] 
**discount** | **float** | Total discount amount for this line | [optional] 
**name** | **str** | Name of the position. Will be displayed instead of the articles name | [optional] 
**price** | **float** | Sales price | [optional] 
**side** | **str** | Side | [optional] 
**uid_manufacturer** | **str** | If the articleId is not specified the article is searched by its manufacturer UID | [optional] 
**variant_id** | **str** | The ID of the variant | [optional] 
**vat_rate** | **float** | VAT rate | [optional] 
**vat_type** | **str** | VAT type (vat_full, vat_reduced, vat_no) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


