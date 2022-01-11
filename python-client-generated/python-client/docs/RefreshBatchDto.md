# RefreshBatchDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**batch_refresh_id** | **str** | The unique ID of the batch | [optional] 
**child_refreshes** | [**list[ConnectionRunDto]**](ConnectionRunDto.md) | The list of jobs initiated by the batch | [optional] 
**created** | **datetime** | When the batch was created, as a datetime | [optional] 
**created_by** | **str** | The ID of the user that created the batch | [optional] 
**destination_status** | **str** | The run status of the destination | [optional] 
**error** | **str** | Any error encountered while initiating the batch | [optional] 
**source_status** | **str** | The run status of the source | [optional] 
**updated** | **datetime** | When the batch was updated, as a datetime | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


