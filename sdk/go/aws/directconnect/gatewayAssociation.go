// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package directconnect

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Associates a Direct Connect Gateway with a VGW.
type GatewayAssociation struct {
	s *pulumi.ResourceState
}

// NewGatewayAssociation registers a new resource with the given unique name, arguments, and options.
func NewGatewayAssociation(ctx *pulumi.Context,
	name string, args *GatewayAssociationArgs, opts ...pulumi.ResourceOpt) (*GatewayAssociation, error) {
	if args == nil || args.DxGatewayId == nil {
		return nil, errors.New("missing required argument 'DxGatewayId'")
	}
	if args == nil || args.VpnGatewayId == nil {
		return nil, errors.New("missing required argument 'VpnGatewayId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["dxGatewayId"] = nil
		inputs["vpnGatewayId"] = nil
	} else {
		inputs["dxGatewayId"] = args.DxGatewayId
		inputs["vpnGatewayId"] = args.VpnGatewayId
	}
	s, err := ctx.RegisterResource("aws:directconnect/gatewayAssociation:GatewayAssociation", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GatewayAssociation{s: s}, nil
}

// GetGatewayAssociation gets an existing GatewayAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetGatewayAssociation(ctx *pulumi.Context,
	name string, id pulumi.ID, state *GatewayAssociationState, opts ...pulumi.ResourceOpt) (*GatewayAssociation, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["dxGatewayId"] = state.DxGatewayId
		inputs["vpnGatewayId"] = state.VpnGatewayId
	}
	s, err := ctx.ReadResource("aws:directconnect/gatewayAssociation:GatewayAssociation", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &GatewayAssociation{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *GatewayAssociation) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *GatewayAssociation) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The ID of the Direct Connect Gateway.
func (r *GatewayAssociation) DxGatewayId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dxGatewayId"])
}

// The ID of the VGW with which to associate the gateway.
func (r *GatewayAssociation) VpnGatewayId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vpnGatewayId"])
}

// Input properties used for looking up and filtering GatewayAssociation resources.
type GatewayAssociationState struct {
	// The ID of the Direct Connect Gateway.
	DxGatewayId interface{}
	// The ID of the VGW with which to associate the gateway.
	VpnGatewayId interface{}
}

// The set of arguments for constructing a GatewayAssociation resource.
type GatewayAssociationArgs struct {
	// The ID of the Direct Connect Gateway.
	DxGatewayId interface{}
	// The ID of the VGW with which to associate the gateway.
	VpnGatewayId interface{}
}
