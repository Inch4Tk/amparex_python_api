# DocumentSearchQuery

Search query used to filter documents

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Test&amp;amp;#42;\&quot; | [optional] 
**document_source_id** | **str** | Find documents for one specific source (eg. InvoiceID) | [optional] 
**from_date** | **date** | Documents from specified date (inclusive) | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**mime_type** | **str** | Search by mime type e.g. \&quot;application/pdf\&quot; | [optional] 
**name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Test&amp;amp;#42;\&quot; | [optional] 
**staff_id** | **str** | Find documents for one specific staff | [optional] 
**to_date** | **date** | Documents to specified date (inclusive) | [optional] 
**treatment_head_id** | **str** | Find documents for one specific treatment | [optional] 
**type_id** | **str** | Find documents of one specific type (PredefinedProperty id) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


