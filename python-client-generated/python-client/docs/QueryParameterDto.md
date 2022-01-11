# QueryParameterDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **str** | The alias of the query parameter, used to avoid name collisions for nested query parameter references | [optional] 
**choices** | **list[object]** | If the query parameter is of type select, this is a list of possible choices. This  is read only and is for listing and viewing reports to help the user. | [optional] 
**id** | **str** | The entity&#39;s unique identifier, set if it is a reference kind. | [optional] 
**label** | **str** | The label for the query parameter | [optional] 
**mode** | **str** | The mode of the query parameter | [optional] 
**name** | **str** | The name of the query parameter | [optional] 
**overridable** | **bool** | Whether the parameter can be overridden, defaults to true. | [optional] 
**reference** | **object** | The hydrated reference object | [optional] 
**select_list_id** | **str** | If mode is select, this must be populated and is a reference to a select list from which choices will be derived. | [optional] 
**type** | **str** | The type of the query parameter | [optional] 
**value** | **object** | The value of the query parameter | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


