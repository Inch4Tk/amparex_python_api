# MarketingActionSearchQuery

Search query used to filter marketingactions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** | find marketingactions by end date | [optional] 
**ident_code** | **str** | find marketingactions by identcode | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**name** | **str** | find marketingactions by name | [optional] 
**not_for_new_customers** | **bool** | find marketingactions (not) available for new customers | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use comment/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**short_name** | **str** | find marketingactions by shortname | [optional] 
**start_date** | **date** | find marketingactions by start date | [optional] 
**system** | **bool** | find marketingactions that are system locked (cannot be modified/deleted) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


