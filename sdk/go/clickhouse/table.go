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

// Resource to manage tables
type Table struct {
	pulumi.CustomResourceState

	// Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
	Cluster pulumi.StringPtrOutput `pulumi:"cluster"`
	// Column
	Columns TableColumnArrayOutput `pulumi:"columns"`
	// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
	Comment pulumi.StringPtrOutput `pulumi:"comment"`
	// DB Name where the table will bellow
	Database pulumi.StringOutput `pulumi:"database"`
	// Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
	Engine pulumi.StringOutput `pulumi:"engine"`
	// Engine params in case the engine type requires them
	EngineParams pulumi.StringArrayOutput `pulumi:"engineParams"`
	// Index
	Indices TableIndexArrayOutput `pulumi:"indices"`
	// Column Name
	Name pulumi.StringOutput `pulumi:"name"`
	// Order by columns to use as sorting key
	OrderBies pulumi.StringArrayOutput `pulumi:"orderBies"`
	// Partition Key to split data
	PartitionBies TablePartitionByArrayOutput `pulumi:"partitionBies"`
	// Table settings
	Settings pulumi.StringMapOutput `pulumi:"settings"`
}

// NewTable registers a new resource with the given unique name, arguments, and options.
func NewTable(ctx *pulumi.Context,
	name string, args *TableArgs, opts ...pulumi.ResourceOption) (*Table, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Database == nil {
		return nil, errors.New("invalid value for required argument 'Database'")
	}
	if args.Engine == nil {
		return nil, errors.New("invalid value for required argument 'Engine'")
	}
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Table
	err := ctx.RegisterResource("clickhouse:index/table:Table", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetTable gets an existing Table resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTable(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *TableState, opts ...pulumi.ResourceOption) (*Table, error) {
	var resource Table
	err := ctx.ReadResource("clickhouse:index/table:Table", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Table resources.
type tableState struct {
	// Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
	Cluster *string `pulumi:"cluster"`
	// Column
	Columns []TableColumn `pulumi:"columns"`
	// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
	Comment *string `pulumi:"comment"`
	// DB Name where the table will bellow
	Database *string `pulumi:"database"`
	// Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
	Engine *string `pulumi:"engine"`
	// Engine params in case the engine type requires them
	EngineParams []string `pulumi:"engineParams"`
	// Index
	Indices []TableIndex `pulumi:"indices"`
	// Column Name
	Name *string `pulumi:"name"`
	// Order by columns to use as sorting key
	OrderBies []string `pulumi:"orderBies"`
	// Partition Key to split data
	PartitionBies []TablePartitionBy `pulumi:"partitionBies"`
	// Table settings
	Settings map[string]string `pulumi:"settings"`
}

type TableState struct {
	// Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
	Cluster pulumi.StringPtrInput
	// Column
	Columns TableColumnArrayInput
	// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
	Comment pulumi.StringPtrInput
	// DB Name where the table will bellow
	Database pulumi.StringPtrInput
	// Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
	Engine pulumi.StringPtrInput
	// Engine params in case the engine type requires them
	EngineParams pulumi.StringArrayInput
	// Index
	Indices TableIndexArrayInput
	// Column Name
	Name pulumi.StringPtrInput
	// Order by columns to use as sorting key
	OrderBies pulumi.StringArrayInput
	// Partition Key to split data
	PartitionBies TablePartitionByArrayInput
	// Table settings
	Settings pulumi.StringMapInput
}

func (TableState) ElementType() reflect.Type {
	return reflect.TypeOf((*tableState)(nil)).Elem()
}

type tableArgs struct {
	// Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
	Cluster *string `pulumi:"cluster"`
	// Column
	Columns []TableColumn `pulumi:"columns"`
	// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
	Comment *string `pulumi:"comment"`
	// DB Name where the table will bellow
	Database string `pulumi:"database"`
	// Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
	Engine string `pulumi:"engine"`
	// Engine params in case the engine type requires them
	EngineParams []string `pulumi:"engineParams"`
	// Index
	Indices []TableIndex `pulumi:"indices"`
	// Column Name
	Name *string `pulumi:"name"`
	// Order by columns to use as sorting key
	OrderBies []string `pulumi:"orderBies"`
	// Partition Key to split data
	PartitionBies []TablePartitionBy `pulumi:"partitionBies"`
	// Table settings
	Settings map[string]string `pulumi:"settings"`
}

// The set of arguments for constructing a Table resource.
type TableArgs struct {
	// Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
	Cluster pulumi.StringPtrInput
	// Column
	Columns TableColumnArrayInput
	// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
	Comment pulumi.StringPtrInput
	// DB Name where the table will bellow
	Database pulumi.StringInput
	// Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
	Engine pulumi.StringInput
	// Engine params in case the engine type requires them
	EngineParams pulumi.StringArrayInput
	// Index
	Indices TableIndexArrayInput
	// Column Name
	Name pulumi.StringPtrInput
	// Order by columns to use as sorting key
	OrderBies pulumi.StringArrayInput
	// Partition Key to split data
	PartitionBies TablePartitionByArrayInput
	// Table settings
	Settings pulumi.StringMapInput
}

func (TableArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*tableArgs)(nil)).Elem()
}

type TableInput interface {
	pulumi.Input

	ToTableOutput() TableOutput
	ToTableOutputWithContext(ctx context.Context) TableOutput
}

func (*Table) ElementType() reflect.Type {
	return reflect.TypeOf((**Table)(nil)).Elem()
}

func (i *Table) ToTableOutput() TableOutput {
	return i.ToTableOutputWithContext(context.Background())
}

func (i *Table) ToTableOutputWithContext(ctx context.Context) TableOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TableOutput)
}

// TableArrayInput is an input type that accepts TableArray and TableArrayOutput values.
// You can construct a concrete instance of `TableArrayInput` via:
//
//	TableArray{ TableArgs{...} }
type TableArrayInput interface {
	pulumi.Input

	ToTableArrayOutput() TableArrayOutput
	ToTableArrayOutputWithContext(context.Context) TableArrayOutput
}

type TableArray []TableInput

func (TableArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Table)(nil)).Elem()
}

func (i TableArray) ToTableArrayOutput() TableArrayOutput {
	return i.ToTableArrayOutputWithContext(context.Background())
}

func (i TableArray) ToTableArrayOutputWithContext(ctx context.Context) TableArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TableArrayOutput)
}

// TableMapInput is an input type that accepts TableMap and TableMapOutput values.
// You can construct a concrete instance of `TableMapInput` via:
//
//	TableMap{ "key": TableArgs{...} }
type TableMapInput interface {
	pulumi.Input

	ToTableMapOutput() TableMapOutput
	ToTableMapOutputWithContext(context.Context) TableMapOutput
}

type TableMap map[string]TableInput

func (TableMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Table)(nil)).Elem()
}

func (i TableMap) ToTableMapOutput() TableMapOutput {
	return i.ToTableMapOutputWithContext(context.Background())
}

func (i TableMap) ToTableMapOutputWithContext(ctx context.Context) TableMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(TableMapOutput)
}

type TableOutput struct{ *pulumi.OutputState }

func (TableOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Table)(nil)).Elem()
}

func (o TableOutput) ToTableOutput() TableOutput {
	return o
}

func (o TableOutput) ToTableOutputWithContext(ctx context.Context) TableOutput {
	return o
}

// Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
func (o TableOutput) Cluster() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Table) pulumi.StringPtrOutput { return v.Cluster }).(pulumi.StringPtrOutput)
}

// Column
func (o TableOutput) Columns() TableColumnArrayOutput {
	return o.ApplyT(func(v *Table) TableColumnArrayOutput { return v.Columns }).(TableColumnArrayOutput)
}

// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
func (o TableOutput) Comment() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Table) pulumi.StringPtrOutput { return v.Comment }).(pulumi.StringPtrOutput)
}

// DB Name where the table will bellow
func (o TableOutput) Database() pulumi.StringOutput {
	return o.ApplyT(func(v *Table) pulumi.StringOutput { return v.Database }).(pulumi.StringOutput)
}

// Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
func (o TableOutput) Engine() pulumi.StringOutput {
	return o.ApplyT(func(v *Table) pulumi.StringOutput { return v.Engine }).(pulumi.StringOutput)
}

// Engine params in case the engine type requires them
func (o TableOutput) EngineParams() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Table) pulumi.StringArrayOutput { return v.EngineParams }).(pulumi.StringArrayOutput)
}

// Index
func (o TableOutput) Indices() TableIndexArrayOutput {
	return o.ApplyT(func(v *Table) TableIndexArrayOutput { return v.Indices }).(TableIndexArrayOutput)
}

// Column Name
func (o TableOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v *Table) pulumi.StringOutput { return v.Name }).(pulumi.StringOutput)
}

// Order by columns to use as sorting key
func (o TableOutput) OrderBies() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Table) pulumi.StringArrayOutput { return v.OrderBies }).(pulumi.StringArrayOutput)
}

// Partition Key to split data
func (o TableOutput) PartitionBies() TablePartitionByArrayOutput {
	return o.ApplyT(func(v *Table) TablePartitionByArrayOutput { return v.PartitionBies }).(TablePartitionByArrayOutput)
}

// Table settings
func (o TableOutput) Settings() pulumi.StringMapOutput {
	return o.ApplyT(func(v *Table) pulumi.StringMapOutput { return v.Settings }).(pulumi.StringMapOutput)
}

type TableArrayOutput struct{ *pulumi.OutputState }

func (TableArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Table)(nil)).Elem()
}

func (o TableArrayOutput) ToTableArrayOutput() TableArrayOutput {
	return o
}

func (o TableArrayOutput) ToTableArrayOutputWithContext(ctx context.Context) TableArrayOutput {
	return o
}

func (o TableArrayOutput) Index(i pulumi.IntInput) TableOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *Table {
		return vs[0].([]*Table)[vs[1].(int)]
	}).(TableOutput)
}

type TableMapOutput struct{ *pulumi.OutputState }

func (TableMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Table)(nil)).Elem()
}

func (o TableMapOutput) ToTableMapOutput() TableMapOutput {
	return o
}

func (o TableMapOutput) ToTableMapOutputWithContext(ctx context.Context) TableMapOutput {
	return o
}

func (o TableMapOutput) MapIndex(k pulumi.StringInput) TableOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *Table {
		return vs[0].(map[string]*Table)[vs[1].(string)]
	}).(TableOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*TableInput)(nil)).Elem(), &Table{})
	pulumi.RegisterInputType(reflect.TypeOf((*TableArrayInput)(nil)).Elem(), TableArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*TableMapInput)(nil)).Elem(), TableMap{})
	pulumi.RegisterOutputType(TableOutput{})
	pulumi.RegisterOutputType(TableArrayOutput{})
	pulumi.RegisterOutputType(TableMapOutput{})
}
