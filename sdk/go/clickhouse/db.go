// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clickhouse

import (
	"context"
	"reflect"

	"github.com/Triple-Whale/pulumi-clickhouse/sdk/go/clickhouse/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource to handle clickhouse databases.
type Db struct {
	pulumi.CustomResourceState

	// Cluster name, not mandatory but should be provided if creating a db in a clustered server
	Cluster pulumi.StringPtrOutput `pulumi:"cluster"`
	// Comment about the database
	Comment pulumi.StringPtrOutput `pulumi:"comment"`
	// Database internal path
	DataPath pulumi.StringOutput `pulumi:"dataPath"`
	// Database engine
	Engine pulumi.StringOutput `pulumi:"engine"`
	// Database internal metadata path
	MetadataPath pulumi.StringOutput `pulumi:"metadataPath"`
	// Database name
	Name pulumi.StringOutput `pulumi:"name"`
	// Database UUID
	Uuid pulumi.StringOutput `pulumi:"uuid"`
}

// NewDb registers a new resource with the given unique name, arguments, and options.
func NewDb(ctx *pulumi.Context,
	name string, args *DbArgs, opts ...pulumi.ResourceOption) (*Db, error) {
	if args == nil {
		args = &DbArgs{}
	}

	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Db
	err := ctx.RegisterResource("clickhouse:index/db:Db", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDb gets an existing Db resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDb(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DbState, opts ...pulumi.ResourceOption) (*Db, error) {
	var resource Db
	err := ctx.ReadResource("clickhouse:index/db:Db", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Db resources.
type dbState struct {
	// Cluster name, not mandatory but should be provided if creating a db in a clustered server
	Cluster *string `pulumi:"cluster"`
	// Comment about the database
	Comment *string `pulumi:"comment"`
	// Database internal path
	DataPath *string `pulumi:"dataPath"`
	// Database engine
	Engine *string `pulumi:"engine"`
	// Database internal metadata path
	MetadataPath *string `pulumi:"metadataPath"`
	// Database name
	Name *string `pulumi:"name"`
	// Database UUID
	Uuid *string `pulumi:"uuid"`
}

type DbState struct {
	// Cluster name, not mandatory but should be provided if creating a db in a clustered server
	Cluster pulumi.StringPtrInput
	// Comment about the database
	Comment pulumi.StringPtrInput
	// Database internal path
	DataPath pulumi.StringPtrInput
	// Database engine
	Engine pulumi.StringPtrInput
	// Database internal metadata path
	MetadataPath pulumi.StringPtrInput
	// Database name
	Name pulumi.StringPtrInput
	// Database UUID
	Uuid pulumi.StringPtrInput
}

func (DbState) ElementType() reflect.Type {
	return reflect.TypeOf((*dbState)(nil)).Elem()
}

type dbArgs struct {
	// Cluster name, not mandatory but should be provided if creating a db in a clustered server
	Cluster *string `pulumi:"cluster"`
	// Comment about the database
	Comment *string `pulumi:"comment"`
	// Database name
	Name *string `pulumi:"name"`
}

// The set of arguments for constructing a Db resource.
type DbArgs struct {
	// Cluster name, not mandatory but should be provided if creating a db in a clustered server
	Cluster pulumi.StringPtrInput
	// Comment about the database
	Comment pulumi.StringPtrInput
	// Database name
	Name pulumi.StringPtrInput
}

func (DbArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dbArgs)(nil)).Elem()
}

type DbInput interface {
	pulumi.Input

	ToDbOutput() DbOutput
	ToDbOutputWithContext(ctx context.Context) DbOutput
}

func (*Db) ElementType() reflect.Type {
	return reflect.TypeOf((**Db)(nil)).Elem()
}

func (i *Db) ToDbOutput() DbOutput {
	return i.ToDbOutputWithContext(context.Background())
}

func (i *Db) ToDbOutputWithContext(ctx context.Context) DbOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbOutput)
}

// DbArrayInput is an input type that accepts DbArray and DbArrayOutput values.
// You can construct a concrete instance of `DbArrayInput` via:
//
//	DbArray{ DbArgs{...} }
type DbArrayInput interface {
	pulumi.Input

	ToDbArrayOutput() DbArrayOutput
	ToDbArrayOutputWithContext(context.Context) DbArrayOutput
}

type DbArray []DbInput

func (DbArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Db)(nil)).Elem()
}

func (i DbArray) ToDbArrayOutput() DbArrayOutput {
	return i.ToDbArrayOutputWithContext(context.Background())
}

func (i DbArray) ToDbArrayOutputWithContext(ctx context.Context) DbArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbArrayOutput)
}

// DbMapInput is an input type that accepts DbMap and DbMapOutput values.
// You can construct a concrete instance of `DbMapInput` via:
//
//	DbMap{ "key": DbArgs{...} }
type DbMapInput interface {
	pulumi.Input

	ToDbMapOutput() DbMapOutput
	ToDbMapOutputWithContext(context.Context) DbMapOutput
}

type DbMap map[string]DbInput

func (DbMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Db)(nil)).Elem()
}

func (i DbMap) ToDbMapOutput() DbMapOutput {
	return i.ToDbMapOutputWithContext(context.Background())
}

func (i DbMap) ToDbMapOutputWithContext(ctx context.Context) DbMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DbMapOutput)
}

type DbOutput struct{ *pulumi.OutputState }

func (DbOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Db)(nil)).Elem()
}

func (o DbOutput) ToDbOutput() DbOutput {
	return o
}

func (o DbOutput) ToDbOutputWithContext(ctx context.Context) DbOutput {
	return o
}

// Cluster name, not mandatory but should be provided if creating a db in a clustered server
func (o DbOutput) Cluster() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Db) pulumi.StringPtrOutput { return v.Cluster }).(pulumi.StringPtrOutput)
}

// Comment about the database
func (o DbOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Db) pulumi.StringPtrOutput { return v.Comment }).(pulumi.StringPtrOutput)
}

// Database internal path
func (o DbOutput) DataPath() pulumi.StringOutput {
	return o.ApplyT(func(v *Db) pulumi.StringOutput { return v.DataPath }).(pulumi.StringOutput)
}

// Database engine
func (o DbOutput) Engine() pulumi.StringOutput {
	return o.ApplyT(func(v *Db) pulumi.StringOutput { return v.Engine }).(pulumi.StringOutput)
}

// Database internal metadata path
func (o DbOutput) MetadataPath() pulumi.StringOutput {
	return o.ApplyT(func(v *Db) pulumi.StringOutput { return v.MetadataPath }).(pulumi.StringOutput)
}

// Database name
func (o DbOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Db) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Database UUID
func (o DbOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v *Db) pulumi.StringOutput { return v.Uuid }).(pulumi.StringOutput)
}

type DbArrayOutput struct{ *pulumi.OutputState }

func (DbArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Db)(nil)).Elem()
}

func (o DbArrayOutput) ToDbArrayOutput() DbArrayOutput {
	return o
}

func (o DbArrayOutput) ToDbArrayOutputWithContext(ctx context.Context) DbArrayOutput {
	return o
}

func (o DbArrayOutput) Index(i pulumi.IntInput) DbOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Db {
		return vs[0].([]*Db)[vs[1].(int)]
	}).(DbOutput)
}

type DbMapOutput struct{ *pulumi.OutputState }

func (DbMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Db)(nil)).Elem()
}

func (o DbMapOutput) ToDbMapOutput() DbMapOutput {
	return o
}

func (o DbMapOutput) ToDbMapOutputWithContext(ctx context.Context) DbMapOutput {
	return o
}

func (o DbMapOutput) MapIndex(k pulumi.StringInput) DbOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Db {
		return vs[0].(map[string]*Db)[vs[1].(string)]
	}).(DbOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*DbInput)(nil)).Elem(), &Db{})
	pulumi.RegisterInputType(reflect.TypeOf((*DbArrayInput)(nil)).Elem(), DbArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*DbMapInput)(nil)).Elem(), DbMap{})
	pulumi.RegisterOutputType(DbOutput{})
	pulumi.RegisterOutputType(DbArrayOutput{})
	pulumi.RegisterOutputType(DbMapOutput{})
}
