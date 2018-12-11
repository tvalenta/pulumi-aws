// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2transitgateway

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages an EC2 Transit Gateway Route.
type Route struct {
	s *pulumi.ResourceState
}

// NewRoute registers a new resource with the given unique name, arguments, and options.
func NewRoute(ctx *pulumi.Context,
	name string, args *RouteArgs, opts ...pulumi.ResourceOpt) (*Route, error) {
	if args == nil || args.DestinationCidrBlock == nil {
		return nil, errors.New("missing required argument 'DestinationCidrBlock'")
	}
	if args == nil || args.TransitGatewayAttachmentId == nil {
		return nil, errors.New("missing required argument 'TransitGatewayAttachmentId'")
	}
	if args == nil || args.TransitGatewayRouteTableId == nil {
		return nil, errors.New("missing required argument 'TransitGatewayRouteTableId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["destinationCidrBlock"] = nil
		inputs["transitGatewayAttachmentId"] = nil
		inputs["transitGatewayRouteTableId"] = nil
	} else {
		inputs["destinationCidrBlock"] = args.DestinationCidrBlock
		inputs["transitGatewayAttachmentId"] = args.TransitGatewayAttachmentId
		inputs["transitGatewayRouteTableId"] = args.TransitGatewayRouteTableId
	}
	s, err := ctx.RegisterResource("aws:ec2transitgateway/route:Route", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Route{s: s}, nil
}

// GetRoute gets an existing Route resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRoute(ctx *pulumi.Context,
	name string, id pulumi.ID, state *RouteState, opts ...pulumi.ResourceOpt) (*Route, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["destinationCidrBlock"] = state.DestinationCidrBlock
		inputs["transitGatewayAttachmentId"] = state.TransitGatewayAttachmentId
		inputs["transitGatewayRouteTableId"] = state.TransitGatewayRouteTableId
	}
	s, err := ctx.ReadResource("aws:ec2transitgateway/route:Route", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Route{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Route) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Route) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
func (r *Route) DestinationCidrBlock() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["destinationCidrBlock"])
}

// Identifier of EC2 Transit Gateway Attachment.
func (r *Route) TransitGatewayAttachmentId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["transitGatewayAttachmentId"])
}

// Identifier of EC2 Transit Gateway Route Table.
func (r *Route) TransitGatewayRouteTableId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["transitGatewayRouteTableId"])
}

// Input properties used for looking up and filtering Route resources.
type RouteState struct {
	// IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
	DestinationCidrBlock interface{}
	// Identifier of EC2 Transit Gateway Attachment.
	TransitGatewayAttachmentId interface{}
	// Identifier of EC2 Transit Gateway Route Table.
	TransitGatewayRouteTableId interface{}
}

// The set of arguments for constructing a Route resource.
type RouteArgs struct {
	// IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
	DestinationCidrBlock interface{}
	// Identifier of EC2 Transit Gateway Attachment.
	TransitGatewayAttachmentId interface{}
	// Identifier of EC2 Transit Gateway Route Table.
	TransitGatewayRouteTableId interface{}
}
