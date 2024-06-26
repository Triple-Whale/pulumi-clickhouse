// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clickhouse

import (
	"context"
	"reflect"

	"errors"
	"github.com/Triple-Whale/pulumi-clickhouse/sdk/go/clickhouse/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The provider type for the clickhouse package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState

	// Default cluster, if provided will be used when no cluster is provided
	DefaultCluster pulumi.StringPtrOutput `pulumi:"defaultCluster"`
	// Clickhouse server url
	Host pulumi.StringOutput `pulumi:"host"`
	// Clickhouse user password with admin privileges
	Password pulumi.StringPtrOutput `pulumi:"password"`
	// Clickhouse username with admin privileges
	Username pulumi.StringPtrOutput `pulumi:"username"`
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Host == nil {
		return nil, errors.New("invalid value for required argument 'Host'")
	}
	if args.Port == nil {
		return nil, errors.New("invalid value for required argument 'Port'")
	}
	if args.Host != nil {
		args.Host = pulumi.ToSecret(args.Host).(pulumi.StringInput)
	}
	if args.Password != nil {
		args.Password = pulumi.ToSecret(args.Password).(pulumi.StringPtrInput)
	}
	secrets := pulumi.AdditionalSecretOutputs([]string{
		"host",
		"password",
	})
	opts = append(opts, secrets)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:clickhouse", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// Default cluster, if provided will be used when no cluster is provided
	DefaultCluster *string `pulumi:"defaultCluster"`
	// Clickhouse server url
	Host string `pulumi:"host"`
	// Clickhouse user password with admin privileges
	Password *string `pulumi:"password"`
	// Clickhouse server native protocol port (TCP)
	Port int `pulumi:"port"`
	// Clickhouse secure connection
	Secure *bool `pulumi:"secure"`
	// Clickhouse username with admin privileges
	Username *string `pulumi:"username"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// Default cluster, if provided will be used when no cluster is provided
	DefaultCluster pulumi.StringPtrInput
	// Clickhouse server url
	Host pulumi.StringInput
	// Clickhouse user password with admin privileges
	Password pulumi.StringPtrInput
	// Clickhouse server native protocol port (TCP)
	Port pulumi.IntInput
	// Clickhouse secure connection
	Secure pulumi.BoolPtrInput
	// Clickhouse username with admin privileges
	Username pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}

type ProviderInput interface {
	pulumi.Input

	ToProviderOutput() ProviderOutput
	ToProviderOutputWithContext(ctx context.Context) ProviderOutput
}

func (*Provider) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (i *Provider) ToProviderOutput() ProviderOutput {
	return i.ToProviderOutputWithContext(context.Background())
}

func (i *Provider) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ProviderOutput)
}

type ProviderOutput struct{ *pulumi.OutputState }

func (ProviderOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Provider)(nil)).Elem()
}

func (o ProviderOutput) ToProviderOutput() ProviderOutput {
	return o
}

func (o ProviderOutput) ToProviderOutputWithContext(ctx context.Context) ProviderOutput {
	return o
}

// Default cluster, if provided will be used when no cluster is provided
func (o ProviderOutput) DefaultCluster() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.DefaultCluster }).(pulumi.StringPtrOutput)
}

// Clickhouse server url
func (o ProviderOutput) Host() pulumi.StringOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringOutput { return v.Host }).(pulumi.StringOutput)
}

// Clickhouse user password with admin privileges
func (o ProviderOutput) Password() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Password }).(pulumi.StringPtrOutput)
}

// Clickhouse username with admin privileges
func (o ProviderOutput) Username() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Provider) pulumi.StringPtrOutput { return v.Username }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ProviderInput)(nil)).Elem(), &Provider{})
	pulumi.RegisterOutputType(ProviderOutput{})
}
