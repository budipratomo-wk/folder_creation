# FolderableDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When the entity was created | [optional] 
**description** | **str** | A description of the folderable entity | [optional] 
**id** | **str** | The UUID unique identifier for the entity. | 
**metadata** | **object** | Contains additional metadata about the entity returned. For example, a table entity might have a type attribute. | [optional] 
**modified** | **datetime** | When a significant event happened on the data object.  For example, for queries, this is when the last run occurred; for tables, this is when the last upload occurred. | [optional] 
**modified_by** | **str** | The identifier of the user who last modified the entity | [optional] 
**name** | **str** | The name of the folderable entity | [optional] 
**parent_id** | **str** | The ID of the folder to which this entity belongs. This can be null if the entity is not in a folder. | [optional] 
**type** | **int** | The numerical identifier for the entity&#39;s type:  Query&#x3D;100, Table&#x3D;200, Pivot View&#x3D;500, Folder&#x3D;600, Shared Table&#x3D;700 | 
**updated** | **datetime** | When the data object was last updated | [optional] 
**updated_by** | **str** | The identifier of the user who last updated the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


