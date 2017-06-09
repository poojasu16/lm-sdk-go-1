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

type GroupData struct {

	NumOfServices int32 `json:"numOfServices,omitempty"`

	AlertStatus string `json:"alertStatus,omitempty"`

	FullPath string `json:"fullPath,omitempty"`

	StopMonitoring bool `json:"stopMonitoring,omitempty"`

	HasServicesDisabled bool `json:"hasServicesDisabled,omitempty"`

	UserPermission string `json:"userPermission,omitempty"`

	Description string `json:"description,omitempty"`

	DisableAlerting bool `json:"disableAlerting,omitempty"`

	SdtStatus string `json:"sdtStatus,omitempty"`

	Name string `json:"name,omitempty"`

	NumOfDirectSubGroups int32 `json:"numOfDirectSubGroups,omitempty"`

	Id int32 `json:"id,omitempty"`

	AlertDisableStatus string `json:"alertDisableStatus,omitempty"`

	NumOfDirectServices int32 `json:"numOfDirectServices,omitempty"`
}
