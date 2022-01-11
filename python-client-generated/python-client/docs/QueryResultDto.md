# QueryResultDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bytes_scanned** | **int** | The number of bytes scanned | [optional] 
**columns** | [**list[ColumnInfoDto]**](ColumnInfoDto.md) | If the query has successfully completed, contains a list of columns and their associated computed types from the query. | [optional] 
**created** | **datetime** | When the entity was created | [optional] 
**duration** | **int** | The duration of time it took to execute the query | [optional] 
**error** | **str** | If an error was encountered during the query, this field will be populated with error text. | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**is_explain** | **bool** | Determines if this query is to be explained and not executed | [optional] 
**parameters** | **dict(str, object)** | The query parameter map | [optional] 
**pivot_status** | **str** | The current status of the pivot execution | [optional] 
**query_dto** | [**QueryDto**](QueryDto.md) | Associated queryDto | [optional] 
**query_id** | **str** | The identifier of the original query | [optional] 
**query_parameters** | [**list[QueryParameterDto]**](QueryParameterDto.md) | Contains the parameters available to the query at the time it was run. This allows consumers to go back in time and view the state of the query at runtime. For older query runs, this value may not be populated. | [optional] 
**query_text** | **str** |  | [optional] 
**rows_returned** | **int** | Contains the number of rows returned from the query. | [optional] 
**size** | **int** | Contains the size of the query results in bytes. This can be used to determine how best to download the file and if it&#39;s reasonable to open it in a browser or other application. This may be 0 if there are no results or the query results were gathered before we started collecting this metric. | [optional] 
**status** | **str** | The current status of the query execution | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


