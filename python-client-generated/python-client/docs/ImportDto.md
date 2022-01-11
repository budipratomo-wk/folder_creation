# ImportDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_mappings** | **dict(str, str)** | a map of import column names to table column ids | [optional] 
**delimiter** | **str** | For overriding the file metadata&#39;s delimiter. The file delimiter is the character to use within the file to separate one field from another. If this value is not set, the import will use the file&#39;s set delimiter. If this value is set, the file metadata&#39;s delimiter will be updated on the file object. | [optional] 
**file_id** | **str** | id of the file to import to the table | 
**metadata** | **dict(str, dict(str, object))** | For overriding column metadata specifically for this import. The keys in this object are column identifiers with the values being metadata objects. | [optional] 
**tags** | **dict(str, str)** | an object containing keys and values, which becomes the tag map | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


