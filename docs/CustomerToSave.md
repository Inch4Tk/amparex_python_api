# CustomerToSave

DTO to save a customer. When creating a new customer, at least surname and firstname are required.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressToSave**](AddressToSave.md) |  | [optional] 
**advertising_flags** | **int** | flags for accepted advertising channels (1&#x3D;Letter 2&#x3D;E-Mail 4&#x3D;Phone 8&#x3D;SMS) / Example: Letter + E-Mail + SMS &#x3D; 1+2+8 &#x3D; 11 | [optional] 
**birthdate** | **str** | Customers birthdate | [optional] 
**customer_nr_extern** | **str** | External identifier of customer | [optional] 
**customer_since** | **str** | Customer in our shop since | [optional] 
**dominant_eye** | **str** | The dominant eye (side_right,side_left) | [optional] 
**dominant_hand** | **str** | The dominant hand (side_right,side_left) | [optional] 
**extension_name** | **str** | Depending on country: Name extension (von, zu) customers middle name (F.) or secondary surname e.g. for spanish names (García) | [optional] 
**first_name** | **str** | Customers first name | [optional] 
**last_visit** | **str** | The date when the customer has last visited the shop | [optional] 
**privacy_statement** | **bool** | Does the customer have already accepted/signed the shops privacy statement? (true&#x3D;accepted, null&#x3D;not yet, false&#x3D;declined) | [optional] 
**privacy_statement_date** | **str** | The date of acceptance/signature of privacy statement | [optional] 
**resp_branch_id** | **str** | The ID of the branch that is responsible for this customer | [optional] 
**resp_staff_id** | **str** | The ID of the staff member responsible for this customer | [optional] 
**restricted_view** | **bool** | TRUE if access to this customer data is restricted to the responsible staff member only. (May be used for VIP persons) | [optional] 
**salutation** | **str** | Customers gender (salutation_missis/salutation_mister/salutation_diverse) | [optional] 
**status_id** | **str** | The ID of the customers status. Use /alias/{alias}/protected/properties/propertytypes/search with name&#x3D;\&quot;propertytype_customer_status\&quot; to get the type-id and then /alias/{alias}/protected/properties/predefinedproperties/search with propertyTypeIDs&#x3D;[\&quot;type-id\&quot;] to get all possible ids and its meaning | [optional] 
**surname** | **str** | Customers last name | [optional] 
**title** | **str** | Customers academic title | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


