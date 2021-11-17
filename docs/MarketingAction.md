# MarketingAction

Information about a marketing action

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**[BranchReduced]**](BranchReduced.md) | which branches this marketing action is available in | [optional] 
**creation** | **datetime** | marketing action creation date and time | [optional] 
**description** | **str** | description | [optional] 
**end_date** | **date** | end date of the marketing action | [optional] 
**id** | **str** |  | [optional] 
**ident_code** | **str** | identification code of the marketing action | [optional] 
**marketing_campaign** | [**MarketingCampaignReduced**](MarketingCampaignReduced.md) |  | [optional] 
**name** | **str** | name of the marketing action | [optional] 
**not_for_new_customers** | **bool** | is this marketing action available for new customers | [optional] 
**referer_program_name** | **str** | name of the program the referer receives | [optional] 
**referred_program_name** | **str** | name of the program the referred receives | [optional] 
**short_name** | **str** | short name of the marketing action | [optional] 
**sort_sequence** | **str** | sort sequence of the marketing action | [optional] 
**start_date** | **date** | start date of the marketing action | [optional] 
**system** | **bool** | is this a system-defined marketing action (cannot be deleted) | [optional] 
**target_description** | **str** | intended goal of the marketing action | [optional] 
**type** | [**PredefinedPropertyReduced**](PredefinedPropertyReduced.md) |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


