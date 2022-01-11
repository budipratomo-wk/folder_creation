# ConnectionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_id** | **str** | The unique ID of the connection | [optional] 
**created** | **datetime** | When the connection was created, as a datetime | [optional] 
**created_by** | **str** | The ID of the user that created the connection | [optional] 
**description** | **str** | The description of the connection, if specified | [optional] 
**destination_id** | **str** | The ID of the file or item the connection sends data to | [optional] 
**destination_type** | **str** | The type of file or item the connection sends data to | [optional] 
**last_run_by** | **str** | The ID of the user that last ran the connection | [optional] 
**last_run_date** | **datetime** | When the connection last ran, as a datetime | [optional] 
**last_run_destination_parameters** | **dict(str, object)** | A map of the parameters used with the destination when the connection last ran | [optional] 
**last_run_job_id** | **str** | The ID of the connection&#39;s last run | [optional] 
**last_run_source_parameters** | **dict(str, object)** | A map of the parameters used with the source when the connection last ran | [optional] 
**metadata** | **dict(str, object)** | Any additional information about the connection | [optional] 
**name** | **str** | The name of the connection, if specified | [optional] 
**source_id** | **str** | The ID of the file or item the connection pulls data from | [optional] 
**source_type** | **str** | The type of file or item the connection pulls data from | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


