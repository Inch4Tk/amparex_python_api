# ServiceContractSearchQuery

Search query used to filter service contracts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** | Searches by using a specific article ID | [optional] 
**customer_ids** | **[str]** | Searches by using multiple customer IDs | [optional] 
**end_date_from** | **date** | Searches service contracts that end after endDateFrom (inclusive) | [optional] 
**end_date_to** | **date** | Searches service contracts that end before endDateTo (inclusive) | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches service contracts that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches service contracts that have last changed before modifiedTo (inclusive) | [optional] 
**numbers** | **[str]** | Searches by using multiple service contract numbers | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use servicecontracts/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**start_date_from** | **date** | Searches service contracts that start after startDateFrom (inclusive) | [optional] 
**start_date_to** | **date** | Searches service contracts that start before startDateTo (inclusive) | [optional] 
**treatment_ids** | **[str]** | Searches by using multiple treatment IDs | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


