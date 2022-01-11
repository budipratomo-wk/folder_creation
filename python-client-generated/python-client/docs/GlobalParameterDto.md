# GlobalParameterDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**choices** | **list[object]** | If the parameter is of type select, this is a list of possible choices. This is read only and is for listing and viewing reports to help the user. | [optional] 
**created** | **datetime** | When the entity was created | [optional] 
**database_id** | **str** | The unique identifier of the database where this parameter can be used to filter query results | [optional] 
**description** | **str** | The description of the parameter | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**label** | **str** | The label for the query parameter | [optional] 
**mode** | **str** | The mode of the parameter | [optional] 
**name** | **str** | The name of the parameter | [optional] 
**overridable** | **bool** | Denotes if this parameter can be overridden later in the process, either when the query is created or executed.  The default is true; it can be overridden. | [optional] 
**select_list_id** | **str** | If mode is select, this must be populated and is a reference to a select list from which choices will be derived. | [optional] 
**type** | **str** | The type of the parameter | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**value** | **object** | The default value of the parameter | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


