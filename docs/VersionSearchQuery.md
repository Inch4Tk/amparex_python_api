# VersionSearchQuery

Search query used to filter versions

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_time_from** | **datetime** | Searches all version that are build after given timestamp | [optional] 
**build_time_to** | **datetime** | Searches all version that are build before given timestamp | [optional] 
**main_version_id** | **str** | Searches for all versions for the corresponding main version | [optional] 
**meta_data** | [**SearchQueryMetaData**](SearchQueryMetaData.md) |  | [optional] 
**number** | **str** | Searches by using a specific release number | [optional] 
**order_by** | [**[OrderBy]**](OrderBy.md) | Multiple order by criteria, use version/orderByFields to get possible values. Use \&quot;ASC\&quot; for ascending, \&quot;DESC\&quot; for descending order; default is \&quot;ASC\&quot;. Maximum 3 order criteria are used. | [optional] 
**release** | **str** | Searches by using major release. e.g. \&quot;LTS-2020.4\&quot; | [optional] 
**stable** | **bool** | Searches for stable / unstable builds | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


