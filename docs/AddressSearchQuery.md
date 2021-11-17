# AddressSearchQuery

Search query used to filter addresss

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_type** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**modified_from** | **datetime** | Searches addresses that have last changed after modifiedFrom (inclusive) | [optional] 
**modified_to** | **datetime** | Searches addresses that have last changed before modifiedTo (inclusive) | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use customer/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**owner_id** | **str** |  | [optional] 
**phone1** | **str** |  | [optional] 
**phone2** | **str** |  | [optional] 
**related_type** | **str** | Related Type of person (B &#x3D; branch,S &#x3D; staff,Y &#x3D; ???,H &#x3D; ???,C &#x3D; Customer,D &#x3D; doctor,X &#x3D; ???) | [optional] 
**street** | **str** |  | [optional] 
**web** | **str** | A URL | [optional] 
**zip** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


