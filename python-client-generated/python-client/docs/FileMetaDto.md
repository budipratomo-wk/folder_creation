# FileMetaDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**column_mappings** | **dict(str, str)** | Maps the columns in the physical file (CSV or JSON) to the columns in fact table &#x3D; {\&quot;physical_col1\&quot;:\&quot;table_col1\&quot;, \&quot;physical_col2\&quot;:\&quot;table_col2\&quot;} | [optional] 
**created** | **datetime** | When the entity was created | [optional] 
**delimiter** | **str** | The character to use as a delimiter within the file to separate one field from another.  The default is comma | [optional] 
**id** | **str** | The entity&#39;s unique identifier | [optional] 
**key** | **str** | The key is here for backwards compatibility only and will always be an empty string. | [optional] 
**metadata** | **dict(str, dict(str, object))** | The file&#39;s meta data | [optional] 
**name** | **str** | The name of the file | [optional] 
**num_errors** | **int** | Number of errors found in the file | [optional] 
**num_records** | **int** | Number of records imported from this file.  This will only be non-zero if the file is in the IMPORTED status. | [optional] 
**original_file_size** | **int** | Size of the original file that was uploaded. | [optional] 
**source** | **str** | URI that describes the source location of this file if imported from another system. For instance, this will have a spreadsheet URL if this file was imported from spreadsheets. This will be null if the file was uploaded using the data prep API. | [optional] 
**status** | **str** | The files&#39;s current status | [optional] 
**table_id** | **str** | The unique identifier for the table | [optional] 
**tags** | **dict(str, str)** | The tags associated with the file | [optional] 
**updated** | **datetime** | When the entity was last updated | [optional] 
**user_id** | **str** | The owner of the entity | [optional] 
**version** | **int** | The version of the current representation of the entity | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


