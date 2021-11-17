# CustomerSearchQuery

Search query used to filter customers

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate_from** | **date** | Searches customers that are born after birthdateFrom (inclusive) | [optional] 
**birthdate_to** | **date** | Searches customers that are born before birthdateTo (inclusive) | [optional] 
**branch_id** | **str** | Searches for exact branchID | [optional] 
**customer_ids** | **[str]** | Searches by using multiple customer IDs | [optional] 
**external_customer_nr** | **str** | Searches by external customer number | [optional] 
**firstname** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches customers that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches customers that have last changed before modifiedTo (inclusive) | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use customer/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**status_ids** | **[str]** | Searches by using multiple predefinedProperty IDs, each of propertyType \&quot;propertytype_customer_status\&quot; | [optional] 
**surname** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


