# MainVersionSearchQuery

Search query used to filter main versions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date_from** | **date** | Searches all main versions that are build after given end date | [optional] 
**end_date_to** | **date** | Searches all main versions that are build before given end date | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**number** | **str** | Searches by using main version number. e.g. \&quot;LTS-2020.4\&quot; | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use mainversion/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**start_date_from** | **date** | Searches all main versions that are build after given start date | [optional] 
**start_date_to** | **date** | Searches all main versions that are build before given start date | [optional] 
**status** | **str** | Searches all main versions for specific status | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


