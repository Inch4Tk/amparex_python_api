# Customer

Detailed information about one customer

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**Address**](Address.md) |  | [optional] 
**advertising_flags** | **int** | 1&#x3D;Letter 2&#x3D;E-Mail 4&#x3D;Phone 8&#x3D;SMS / Example: Letter + E-Mail + SMS &#x3D; 1+2+8 &#x3D; 11 | [optional] 
**anonymized_at** | **date** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**branch_id** | **str** | The branchID a customer is assigned to | [optional] 
**customer_nr** | **int** |  | [optional] 
**customer_nr_external** | **str** | A customer nr sometimes used in addition to the normal customer nr | [optional] 
**customer_since** | **date** |  | [optional] 
**dominant_eye** | **str** |  | [optional] 
**dominant_hand** | **str** |  | [optional] 
**extension_name** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**health_insurance** | [**HealthInsuranceReduced**](HealthInsuranceReduced.md) |  | [optional] 
**hi_membership_id** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**last_visit** | **date** |  | [optional] 
**marketing_action** | **str** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**privacy_statement** | **bool** | State of privacy statment: TRUE &#x3D; acceptec, FALSE &#x3D; declined, NULL &#x3D; open | [optional] 
**privacy_statement_date** | **date** | Date when the customer has accepted the privacy statement | [optional] 
**restricted_view** | **bool** |  | [optional] 
**salutation** | [**TranslatedString**](TranslatedString.md) |  | [optional] 
**social_security_number** | **str** | The social security number of the customer | [optional] 
**staff_id** | **str** | The staffID a customer is assigned to | [optional] 
**status** | [**PredefinedPropertyReduced**](PredefinedPropertyReduced.md) |  | [optional] 
**surname** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


