# SharedTableDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When the entity was created | [optional] 
**destination_workspace_id** | **str** | The id of the workspace being shared to. | 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**parent_id** | **str** | If non-null, indicates the parent of this entity. Must be modified through the folder api. | [optional] 
**source_table_id** | **str** | The id of the table being shared. | 
**table** | [**TableDto**](TableDto.md) | The associated table which will be hydrated when listing are fetching shared table entities. | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


