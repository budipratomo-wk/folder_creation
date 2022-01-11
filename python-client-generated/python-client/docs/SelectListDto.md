# SelectListDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When the entity was created | [optional] 
**description** | **str** | Description of this select list. Max length: 1024 | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**name** | **str** | Name of this select list. Max length: 100 | [optional] 
**type** | **str** | This is currently not used and its value will always be &#39;static&#39;. In the future, more types will be added. | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**value_type** | **str** | Defines the type of the items in the list. | [optional] 
**values** | **list[object]** | List of possible values for the list. These values will be validated against the valueType provided. | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


