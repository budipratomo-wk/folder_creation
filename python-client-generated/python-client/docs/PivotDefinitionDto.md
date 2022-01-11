# PivotDefinitionDto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**columns** | [**list[PivotViewDefinitionColumnDto]**](PivotViewDefinitionColumnDto.md) | The colmnnns associated with the pivot view | [optional] 
**decimal_places** | **int** | Numeric data values are rounded to the number of decimal places.  The default number to round to and show is 2 decimal places, and the maximum number is capped at 16. | [optional] 
**filters** | [**list[PivotViewDefinitionFilterDto]**](PivotViewDefinitionFilterDto.md) | The filters associated with the pivot view | [optional] 
**grand_total_enabled** | **str** | The level to which Grand Totals are enabled.  It is defaulted to DISABLED. | [optional] 
**id** | **str** | The pivot view&#39;s definition&#39;s id | [optional] 
**multiple_headers** | **bool** | Denotes whether a pivot is created in multi-line header mode. Default is false. | [optional] 
**pivot_view_type** | **str** | The type of pivot view. Options are currently Classic and Compact. | [optional] 
**rows** | [**list[PivotViewDefinitionRowDto]**](PivotViewDefinitionRowDto.md) | The rows associated with the pivot view | [optional] 
**sort_columns** | **list[str]** | Columns with which to sort the crosstab query | [optional] 
**subtotal_enabled** | **str** | The level to which Subtotals are enabled.  It is defaulted to DISABLED. | [optional] 
**values** | [**list[PivotViewDefinitionValueDto]**](PivotViewDefinitionValueDto.md) | The values associated with the pivot view | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


