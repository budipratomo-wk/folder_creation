# ValidateFilesDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_files** | [**list[FileMetaDto]**](FileMetaDto.md) | A list of files that were deleted during the validation because not enough information was available to repair them. These files will no longer be available via the endpoint and will not be included in queries. | [optional] 
**repaired_files** | [**list[FileMetaDto]**](FileMetaDto.md) | A list of files that were modified during the validation and will continue to be visible and to be usable in the account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


