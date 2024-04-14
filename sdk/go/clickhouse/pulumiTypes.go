// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clickhouse

import (
	"context"
	"reflect"

	"github.com/Triple-Whale/pulumi-clickhouse/sdk/go/clickhouse/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type TableColumn struct {
	// Column Name
	Name string `pulumi:"name"`
	// Column Type
	Type string `pulumi:"type"`
}

// TableColumnInput is an input type that accepts TableColumnArgs and TableColumnOutput values.
// You can construct a concrete instance of `TableColumnInput` via:
//
//	TableColumnArgs{...}
type TableColumnInput interface {
	pulumi.Input

	ToTableColumnOutput() TableColumnOutput
	ToTableColumnOutputWithContext(context.Context) TableColumnOutput
}

type TableColumnArgs struct {
	// Column Name
	Name pulumi.StringInput `pulumi:"name"`
	// Column Type
	Type pulumi.StringInput `pulumi:"type"`
}

func (TableColumnArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TableColumn)(nil)).Elem()
}

func (i TableColumnArgs) ToTableColumnOutput() TableColumnOutput {
	return i.ToTableColumnOutputWithContext(context.Background())
}

func (i TableColumnArgs) ToTableColumnOutputWithContext(ctx context.Context) TableColumnOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TableColumnOutput)
}

// TableColumnArrayInput is an input type that accepts TableColumnArray and TableColumnArrayOutput values.
// You can construct a concrete instance of `TableColumnArrayInput` via:
//
//	TableColumnArray{ TableColumnArgs{...} }
type TableColumnArrayInput interface {
	pulumi.Input

	ToTableColumnArrayOutput() TableColumnArrayOutput
	ToTableColumnArrayOutputWithContext(context.Context) TableColumnArrayOutput
}

type TableColumnArray []TableColumnInput

func (TableColumnArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TableColumn)(nil)).Elem()
}

func (i TableColumnArray) ToTableColumnArrayOutput() TableColumnArrayOutput {
	return i.ToTableColumnArrayOutputWithContext(context.Background())
}

func (i TableColumnArray) ToTableColumnArrayOutputWithContext(ctx context.Context) TableColumnArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TableColumnArrayOutput)
}

type TableColumnOutput struct{ *pulumi.OutputState }

func (TableColumnOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TableColumn)(nil)).Elem()
}

func (o TableColumnOutput) ToTableColumnOutput() TableColumnOutput {
	return o
}

func (o TableColumnOutput) ToTableColumnOutputWithContext(ctx context.Context) TableColumnOutput {
	return o
}

// Column Name
func (o TableColumnOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v TableColumn) string { return v.Name }).(pulumi.StringOutput)
}

// Column Type
func (o TableColumnOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v TableColumn) string { return v.Type }).(pulumi.StringOutput)
}

type TableColumnArrayOutput struct{ *pulumi.OutputState }

func (TableColumnArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TableColumn)(nil)).Elem()
}

func (o TableColumnArrayOutput) ToTableColumnArrayOutput() TableColumnArrayOutput {
	return o
}

func (o TableColumnArrayOutput) ToTableColumnArrayOutputWithContext(ctx context.Context) TableColumnArrayOutput {
	return o
}

func (o TableColumnArrayOutput) Index(i pulumi.IntInput) TableColumnOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) TableColumn {
		return vs[0].([]TableColumn)[vs[1].(int)]
	}).(TableColumnOutput)
}

type TablePartitionBy struct {
	// Column to use as part of the partition key
	By string `pulumi:"by"`
	// Partition function, could be empty or one of following: toYYYYMM, toYYYYMMDD or toYYYYMMDDhhmmss
	PartitionFunction *string `pulumi:"partitionFunction"`
}

// TablePartitionByInput is an input type that accepts TablePartitionByArgs and TablePartitionByOutput values.
// You can construct a concrete instance of `TablePartitionByInput` via:
//
//	TablePartitionByArgs{...}
type TablePartitionByInput interface {
	pulumi.Input

	ToTablePartitionByOutput() TablePartitionByOutput
	ToTablePartitionByOutputWithContext(context.Context) TablePartitionByOutput
}

type TablePartitionByArgs struct {
	// Column to use as part of the partition key
	By pulumi.StringInput `pulumi:"by"`
	// Partition function, could be empty or one of following: toYYYYMM, toYYYYMMDD or toYYYYMMDDhhmmss
	PartitionFunction pulumi.StringPtrInput `pulumi:"partitionFunction"`
}

func (TablePartitionByArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*TablePartitionBy)(nil)).Elem()
}

func (i TablePartitionByArgs) ToTablePartitionByOutput() TablePartitionByOutput {
	return i.ToTablePartitionByOutputWithContext(context.Background())
}

func (i TablePartitionByArgs) ToTablePartitionByOutputWithContext(ctx context.Context) TablePartitionByOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TablePartitionByOutput)
}

// TablePartitionByArrayInput is an input type that accepts TablePartitionByArray and TablePartitionByArrayOutput values.
// You can construct a concrete instance of `TablePartitionByArrayInput` via:
//
//	TablePartitionByArray{ TablePartitionByArgs{...} }
type TablePartitionByArrayInput interface {
	pulumi.Input

	ToTablePartitionByArrayOutput() TablePartitionByArrayOutput
	ToTablePartitionByArrayOutputWithContext(context.Context) TablePartitionByArrayOutput
}

type TablePartitionByArray []TablePartitionByInput

func (TablePartitionByArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TablePartitionBy)(nil)).Elem()
}

func (i TablePartitionByArray) ToTablePartitionByArrayOutput() TablePartitionByArrayOutput {
	return i.ToTablePartitionByArrayOutputWithContext(context.Background())
}

func (i TablePartitionByArray) ToTablePartitionByArrayOutputWithContext(ctx context.Context) TablePartitionByArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TablePartitionByArrayOutput)
}

type TablePartitionByOutput struct{ *pulumi.OutputState }

func (TablePartitionByOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*TablePartitionBy)(nil)).Elem()
}

func (o TablePartitionByOutput) ToTablePartitionByOutput() TablePartitionByOutput {
	return o
}

func (o TablePartitionByOutput) ToTablePartitionByOutputWithContext(ctx context.Context) TablePartitionByOutput {
	return o
}

// Column to use as part of the partition key
func (o TablePartitionByOutput) By() pulumi.StringOutput {
	return o.ApplyT(func(v TablePartitionBy) string { return v.By }).(pulumi.StringOutput)
}

// Partition function, could be empty or one of following: toYYYYMM, toYYYYMMDD or toYYYYMMDDhhmmss
func (o TablePartitionByOutput) PartitionFunction() pulumi.StringPtrOutput {
	return o.ApplyT(func(v TablePartitionBy) *string { return v.PartitionFunction }).(pulumi.StringPtrOutput)
}

type TablePartitionByArrayOutput struct{ *pulumi.OutputState }

func (TablePartitionByArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]TablePartitionBy)(nil)).Elem()
}

func (o TablePartitionByArrayOutput) ToTablePartitionByArrayOutput() TablePartitionByArrayOutput {
	return o
}

func (o TablePartitionByArrayOutput) ToTablePartitionByArrayOutputWithContext(ctx context.Context) TablePartitionByArrayOutput {
	return o
}

func (o TablePartitionByArrayOutput) Index(i pulumi.IntInput) TablePartitionByOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) TablePartitionBy {
		return vs[0].([]TablePartitionBy)[vs[1].(int)]
	}).(TablePartitionByOutput)
}

type GetDbsDb struct {
	Comment      string `pulumi:"comment"`
	DataPath     string `pulumi:"dataPath"`
	Engine       string `pulumi:"engine"`
	MetadataPath string `pulumi:"metadataPath"`
	Name         string `pulumi:"name"`
	Uuid         string `pulumi:"uuid"`
}

// GetDbsDbInput is an input type that accepts GetDbsDbArgs and GetDbsDbOutput values.
// You can construct a concrete instance of `GetDbsDbInput` via:
//
//	GetDbsDbArgs{...}
type GetDbsDbInput interface {
	pulumi.Input

	ToGetDbsDbOutput() GetDbsDbOutput
	ToGetDbsDbOutputWithContext(context.Context) GetDbsDbOutput
}

type GetDbsDbArgs struct {
	Comment      pulumi.StringInput `pulumi:"comment"`
	DataPath     pulumi.StringInput `pulumi:"dataPath"`
	Engine       pulumi.StringInput `pulumi:"engine"`
	MetadataPath pulumi.StringInput `pulumi:"metadataPath"`
	Name         pulumi.StringInput `pulumi:"name"`
	Uuid         pulumi.StringInput `pulumi:"uuid"`
}

func (GetDbsDbArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDbsDb)(nil)).Elem()
}

func (i GetDbsDbArgs) ToGetDbsDbOutput() GetDbsDbOutput {
	return i.ToGetDbsDbOutputWithContext(context.Background())
}

func (i GetDbsDbArgs) ToGetDbsDbOutputWithContext(ctx context.Context) GetDbsDbOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetDbsDbOutput)
}

// GetDbsDbArrayInput is an input type that accepts GetDbsDbArray and GetDbsDbArrayOutput values.
// You can construct a concrete instance of `GetDbsDbArrayInput` via:
//
//	GetDbsDbArray{ GetDbsDbArgs{...} }
type GetDbsDbArrayInput interface {
	pulumi.Input

	ToGetDbsDbArrayOutput() GetDbsDbArrayOutput
	ToGetDbsDbArrayOutputWithContext(context.Context) GetDbsDbArrayOutput
}

type GetDbsDbArray []GetDbsDbInput

func (GetDbsDbArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetDbsDb)(nil)).Elem()
}

func (i GetDbsDbArray) ToGetDbsDbArrayOutput() GetDbsDbArrayOutput {
	return i.ToGetDbsDbArrayOutputWithContext(context.Background())
}

func (i GetDbsDbArray) ToGetDbsDbArrayOutputWithContext(ctx context.Context) GetDbsDbArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetDbsDbArrayOutput)
}

type GetDbsDbOutput struct{ *pulumi.OutputState }

func (GetDbsDbOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetDbsDb)(nil)).Elem()
}

func (o GetDbsDbOutput) ToGetDbsDbOutput() GetDbsDbOutput {
	return o
}

func (o GetDbsDbOutput) ToGetDbsDbOutputWithContext(ctx context.Context) GetDbsDbOutput {
	return o
}

func (o GetDbsDbOutput) Comment() pulumi.StringOutput {
	return o.ApplyT(func(v GetDbsDb) string { return v.Comment }).(pulumi.StringOutput)
}

func (o GetDbsDbOutput) DataPath() pulumi.StringOutput {
	return o.ApplyT(func(v GetDbsDb) string { return v.DataPath }).(pulumi.StringOutput)
}

func (o GetDbsDbOutput) Engine() pulumi.StringOutput {
	return o.ApplyT(func(v GetDbsDb) string { return v.Engine }).(pulumi.StringOutput)
}

func (o GetDbsDbOutput) MetadataPath() pulumi.StringOutput {
	return o.ApplyT(func(v GetDbsDb) string { return v.MetadataPath }).(pulumi.StringOutput)
}

func (o GetDbsDbOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetDbsDb) string { return v.Name }).(pulumi.StringOutput)
}

func (o GetDbsDbOutput) Uuid() pulumi.StringOutput {
	return o.ApplyT(func(v GetDbsDb) string { return v.Uuid }).(pulumi.StringOutput)
}

type GetDbsDbArrayOutput struct{ *pulumi.OutputState }

func (GetDbsDbArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetDbsDb)(nil)).Elem()
}

func (o GetDbsDbArrayOutput) ToGetDbsDbArrayOutput() GetDbsDbArrayOutput {
	return o
}

func (o GetDbsDbArrayOutput) ToGetDbsDbArrayOutputWithContext(ctx context.Context) GetDbsDbArrayOutput {
	return o
}

func (o GetDbsDbArrayOutput) Index(i pulumi.IntInput) GetDbsDbOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetDbsDb {
		return vs[0].([]GetDbsDb)[vs[1].(int)]
	}).(GetDbsDbOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TableColumnInput)(nil)).Elem(), TableColumnArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TableColumnArrayInput)(nil)).Elem(), TableColumnArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TablePartitionByInput)(nil)).Elem(), TablePartitionByArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*TablePartitionByArrayInput)(nil)).Elem(), TablePartitionByArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetDbsDbInput)(nil)).Elem(), GetDbsDbArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*GetDbsDbArrayInput)(nil)).Elem(), GetDbsDbArray{})
	pulumi.RegisterOutputType(TableColumnOutput{})
	pulumi.RegisterOutputType(TableColumnArrayOutput{})
	pulumi.RegisterOutputType(TablePartitionByOutput{})
	pulumi.RegisterOutputType(TablePartitionByArrayOutput{})
	pulumi.RegisterOutputType(GetDbsDbOutput{})
	pulumi.RegisterOutputType(GetDbsDbArrayOutput{})
}
