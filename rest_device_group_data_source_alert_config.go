/* 
 * 
 *
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.0.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 */

package logicmonitor

type RestDeviceGroupDataSourceAlertConfig struct {

	DatasourceType string `json:"datasourceType,omitempty"`

	DpConfig []DataPointConfig `json:"dpConfig,omitempty"`
}
