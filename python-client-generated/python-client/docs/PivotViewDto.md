# PivotViewDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_meta** | **dict(str, object)** | User-defined metadata to attach to the pivot view. This is any arbitrary JSON object and is not required. | [optional] 
**created** | **datetime** | When the entity was created | [optional] 
**description** | **str** | The description of the pivot view | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**name** | **str** | Name of the pivot view. The maximum size is 255 characters. | 
**parent_id** | **str** | If non-null, indicates the parent of this entity. Must be modified through the folder api. | [optional] 
**query_id** | **str** | The query to associate with this pivot view. This value is required and cannot be updated after the pivot is created. Any attempt to update the query ID is ignored. | 
**query_result_id** | **str** | An optional query result id to associate with this pivot view. If associated, saving a pivot view will cause an existence check on the related query result.  This value is not required. The query id on the query result must match this pivot&#39;s query ID. | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


