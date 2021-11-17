# MarketingContactSearchQuery

Search query used to filter marketingcontacts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_from** | **datetime** | Searches marketing contacts that have been created after &#39;createdFrom&#39; (inclusive) | [optional] 
**created_to** | **datetime** | Searches marketing contacts that have been created before &#39;createdTo&#39; (inclusive) | [optional] 
**marketing_action_id** | **str** | Searches for exact marketingActionID | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use marketingcontact/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**person_id** | **str** | Searches for exact personID | [optional] 
**staff_id** | **str** | Searches for exact staffID | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


