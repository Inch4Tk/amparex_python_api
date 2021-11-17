# DoctorSearchQuery

Search query used to filter doctors

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate** | **date** |  | [optional] 
**business_name** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**business_premises_number** | **str** |  | [optional] 
**dentist** | **bool** |  | [optional] 
**doctor_number** | **str** |  | [optional] 
**doctor_seq_nr** | **int** |  | [optional] 
**firstname** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**ik_number** | **str** | Filter by specific IK-Number | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use doctor/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**post_nominal** | **str** |  | [optional] 
**surname** | **str** | Wildcard search could be used with &#39;&amp;amp;#42;&#39;,  for example \&quot;Xyz&amp;amp;#42;\&quot; | [optional] 
**used** | **bool** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


