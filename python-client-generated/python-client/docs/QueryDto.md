# QueryDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When the entity was created | [optional] 
**definition** | [**PivotDefinitionDto**](PivotDefinitionDto.md) | The pivot view&#39;s definition | [optional] 
**dependencies** | [**list[QueryDependencyDto]**](QueryDependencyDto.md) | A structured list of dependencies that this query relies upon. This list is populated by the server from the query text. Each dependency model contains enough information to find the source object. | [optional] 
**description** | **str** | The description of the query | [optional] 
**history_revision** | **int** | Historical revision number of this entity | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**last_run** | **datetime** | If non-null, indicates the last time this query was run. | [optional] 
**last_run_by** | **str** | If non-null, indicates the last user that ran the query. | [optional] 
**name** | **str** | The name of the query | [optional] 
**parameters** | [**list[QueryParameterDto]**](QueryParameterDto.md) | The query parameters | [optional] 
**parent_id** | **str** | If non-null, indicates the parent of this entity. Must be modified through the folder api. | [optional] 
**primary_query_result_id** | **str** | The identifier of the primary query result | [optional] 
**query_text** | **str** | Max size is 30000 characters.  Is required.  Must be a valid DML statement. | 
**temporary** | **bool** | Denotes if this query is meant to be temporary.  Default is false. | [optional] 
**type** | **str** | This field exists for backwards compatibility only and will always be an empty string. | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


