// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pinpoint

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type ApnsVoipChannel struct {
	s *pulumi.ResourceState
}

// NewApnsVoipChannel registers a new resource with the given unique name, arguments, and options.
func NewApnsVoipChannel(ctx *pulumi.Context,
	name string, args *ApnsVoipChannelArgs, opts ...pulumi.ResourceOpt) (*ApnsVoipChannel, error) {
	if args == nil || args.ApplicationId == nil {
		return nil, errors.New("missing required argument 'ApplicationId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["applicationId"] = nil
		inputs["bundleId"] = nil
		inputs["certificate"] = nil
		inputs["defaultAuthenticationMethod"] = nil
		inputs["enabled"] = nil
		inputs["privateKey"] = nil
		inputs["teamId"] = nil
		inputs["tokenKey"] = nil
		inputs["tokenKeyId"] = nil
	} else {
		inputs["applicationId"] = args.ApplicationId
		inputs["bundleId"] = args.BundleId
		inputs["certificate"] = args.Certificate
		inputs["defaultAuthenticationMethod"] = args.DefaultAuthenticationMethod
		inputs["enabled"] = args.Enabled
		inputs["privateKey"] = args.PrivateKey
		inputs["teamId"] = args.TeamId
		inputs["tokenKey"] = args.TokenKey
		inputs["tokenKeyId"] = args.TokenKeyId
	}
	s, err := ctx.RegisterResource("aws:pinpoint/apnsVoipChannel:ApnsVoipChannel", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ApnsVoipChannel{s: s}, nil
}

// GetApnsVoipChannel gets an existing ApnsVoipChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApnsVoipChannel(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ApnsVoipChannelState, opts ...pulumi.ResourceOpt) (*ApnsVoipChannel, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["applicationId"] = state.ApplicationId
		inputs["bundleId"] = state.BundleId
		inputs["certificate"] = state.Certificate
		inputs["defaultAuthenticationMethod"] = state.DefaultAuthenticationMethod
		inputs["enabled"] = state.Enabled
		inputs["privateKey"] = state.PrivateKey
		inputs["teamId"] = state.TeamId
		inputs["tokenKey"] = state.TokenKey
		inputs["tokenKeyId"] = state.TokenKeyId
	}
	s, err := ctx.ReadResource("aws:pinpoint/apnsVoipChannel:ApnsVoipChannel", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ApnsVoipChannel{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ApnsVoipChannel) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ApnsVoipChannel) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *ApnsVoipChannel) ApplicationId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["applicationId"])
}

func (r *ApnsVoipChannel) BundleId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["bundleId"])
}

func (r *ApnsVoipChannel) Certificate() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["certificate"])
}

func (r *ApnsVoipChannel) DefaultAuthenticationMethod() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["defaultAuthenticationMethod"])
}

func (r *ApnsVoipChannel) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

func (r *ApnsVoipChannel) PrivateKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["privateKey"])
}

func (r *ApnsVoipChannel) TeamId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["teamId"])
}

func (r *ApnsVoipChannel) TokenKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tokenKey"])
}

func (r *ApnsVoipChannel) TokenKeyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tokenKeyId"])
}

// Input properties used for looking up and filtering ApnsVoipChannel resources.
type ApnsVoipChannelState struct {
	ApplicationId interface{}
	BundleId interface{}
	Certificate interface{}
	DefaultAuthenticationMethod interface{}
	Enabled interface{}
	PrivateKey interface{}
	TeamId interface{}
	TokenKey interface{}
	TokenKeyId interface{}
}

// The set of arguments for constructing a ApnsVoipChannel resource.
type ApnsVoipChannelArgs struct {
	ApplicationId interface{}
	BundleId interface{}
	Certificate interface{}
	DefaultAuthenticationMethod interface{}
	Enabled interface{}
	PrivateKey interface{}
	TeamId interface{}
	TokenKey interface{}
	TokenKeyId interface{}
}
