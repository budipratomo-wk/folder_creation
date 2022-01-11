# ValidateTablesDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deleted_tables** | [**list[TableDto]**](TableDto.md) | A list of tables that were deleted during the validation because not enough information was available to repair them. These tables will no longer be available via the endpoint and queries using these tables will cease to function properly. | [optional] 
**repaired_tables** | [**list[TableDto]**](TableDto.md) | A list of tables that were modified during the validation and will continue to be visible and to be usable in the account. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


