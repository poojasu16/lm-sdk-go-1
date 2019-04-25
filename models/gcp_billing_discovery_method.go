// Code generated by go-swagger; DO NOT EDIT.

package models

// This file was generated by the swagger tool.
// Editing this file might prove futile when you re-run the swagger generate command

import (
	"bytes"
	"encoding/json"

	strfmt "github.com/go-openapi/strfmt"

	"github.com/go-openapi/errors"
	"github.com/go-openapi/swag"
	"github.com/go-openapi/validate"
)

// GcpBillingDiscoveryMethod gcp billing discovery method
// swagger:model GcpBillingDiscoveryMethod
type GcpBillingDiscoveryMethod struct {

	// gcp billing type
	// Required: true
	GcpBillingType *string `json:"gcpBillingType"`
}

// Name gets the name of this subtype
func (m *GcpBillingDiscoveryMethod) Name() string {
	return "GcpBillingDiscoveryMethod"
}

// SetName sets the name of this subtype
func (m *GcpBillingDiscoveryMethod) SetName(val string) {

}

// GcpBillingType gets the gcp billing type of this subtype

// UnmarshalJSON unmarshals this object with a polymorphic type from a JSON structure
func (m *GcpBillingDiscoveryMethod) UnmarshalJSON(raw []byte) error {
	var data struct {

		// gcp billing type
		// Required: true
		GcpBillingType *string `json:"gcpBillingType"`
	}
	buf := bytes.NewBuffer(raw)
	dec := json.NewDecoder(buf)
	dec.UseNumber()

	if err := dec.Decode(&data); err != nil {
		return err
	}

	var base struct {
		/* Just the base type fields. Used for unmashalling polymorphic types.*/

		Name string `json:"name"`
	}
	buf = bytes.NewBuffer(raw)
	dec = json.NewDecoder(buf)
	dec.UseNumber()

	if err := dec.Decode(&base); err != nil {
		return err
	}

	var result GcpBillingDiscoveryMethod

	if base.Name != result.Name() {
		/* Not the type we're looking for. */
		return errors.New(422, "invalid name value: %q", base.Name)
	}

	result.GcpBillingType = data.GcpBillingType

	*m = result

	return nil
}

// MarshalJSON marshals this object with a polymorphic type to a JSON structure
func (m GcpBillingDiscoveryMethod) MarshalJSON() ([]byte, error) {
	var b1, b2, b3 []byte
	var err error
	b1, err = json.Marshal(struct {

		// gcp billing type
		// Required: true
		GcpBillingType *string `json:"gcpBillingType"`
	}{

		GcpBillingType: m.GcpBillingType,
	},
	)
	if err != nil {
		return nil, err
	}
	b2, err = json.Marshal(struct {
		Name string `json:"name"`
	}{

		Name: m.Name(),
	},
	)
	if err != nil {
		return nil, err
	}

	return swag.ConcatJSON(b1, b2, b3), nil
}

// Validate validates this gcp billing discovery method
func (m *GcpBillingDiscoveryMethod) Validate(formats strfmt.Registry) error {
	var res []error

	if err := m.validateGcpBillingType(formats); err != nil {
		res = append(res, err)
	}

	if len(res) > 0 {
		return errors.CompositeValidationError(res...)
	}
	return nil
}

func (m *GcpBillingDiscoveryMethod) validateGcpBillingType(formats strfmt.Registry) error {

	if err := validate.Required("gcpBillingType", "body", m.GcpBillingType); err != nil {
		return err
	}

	return nil
}

// MarshalBinary interface implementation
func (m *GcpBillingDiscoveryMethod) MarshalBinary() ([]byte, error) {
	if m == nil {
		return nil, nil
	}
	return swag.WriteJSON(m)
}

// UnmarshalBinary interface implementation
func (m *GcpBillingDiscoveryMethod) UnmarshalBinary(b []byte) error {
	var res GcpBillingDiscoveryMethod
	if err := swag.ReadJSON(b, &res); err != nil {
		return err
	}
	*m = res
	return nil
}
