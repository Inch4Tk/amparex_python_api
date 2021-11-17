# ItemsToTransfer

Source and target branch, items to transfer an destination status and notice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_branch_id** | **str** | Branch id where items are to be moved in | [optional] 
**destination_status** | **str** | The destination status (ai_state_transfer,ai_state_stock). ai_state_transfer (default) -&amp;gt; branch has to accept the items, ai_state_stock items -&amp;gt; are immediate in destination stock | [optional] 
**items** | [**[ItemRef]**](ItemRef.md) | List of items to move from source- to destination-branch | [optional] 
**notice** | **str** | Notice for delivery note and item move entries | [optional] 
**source_branch_id** | **str** | Branch id where items are searched for (default is login-branch) | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


