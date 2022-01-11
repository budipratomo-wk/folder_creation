# TableDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When the entity was created | [optional] 
**database_id** | **str** | The unique identifier of the database where the table resides. | [optional] 
**dataset_updated** | **datetime** | The last time that the data set for this table was modified. | [optional] 
**deleted** | **bool** | This is for backwards compatibility only and will always return false. | [optional] 
**description** | **str** | May be at most 255 characters in length | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**is_shared** | **bool** | A property indicating if this table is shared to any destination. | 
**last_uploaded** | **datetime** | Contains the date and time of the last file that was imported into the table. Valuable for determining if the data is stale. | [optional] 
**name** | **str** | May be at most 150 characters in length | [optional] 
**parent_id** | **str** | If non-null, indicates the parent of this entity. Must be modified through the folder api. | [optional] 
**read_only** | **bool** | Indicates if this table is readonly in the account receiving this table. If so, any attempt to edit the table will fail. | [optional] 
**table_schema** | [**TableSchema**](TableSchema.md) | The schema to apply | [optional] 
**type** | **str** | The type of table | [optional] 
**unique_table_constraints** | [**list[UniqueConstraintDto]**](UniqueConstraintDto.md) | A property indicating the unique constraints on the table. | 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


