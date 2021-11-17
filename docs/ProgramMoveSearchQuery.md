# ProgramMoveSearchQuery

Search query used to filter program moves

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**article_id** | **str** | Find program moves for given article id | [optional] 
**article_name_like** | **str** | Find program moves for article name like | [optional] 
**branch_id** | **str** | Find program moves for given branch id | [optional] 
**hours_back** | **int** | Find program moves for last x hours | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use comment/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**program_name_like** | **str** | Find program moves for program name like | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


