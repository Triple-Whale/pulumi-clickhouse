// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Resource to manage tables
 */
export class Table extends pulumi.CustomResource {
    /**
     * Get an existing Table resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState, opts?: pulumi.CustomResourceOptions): Table {
        return new Table(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'clickhouse:index/table:Table';

    /**
     * Returns true if the given object is an instance of Table.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Table {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Table.__pulumiType;
    }

    /**
     * Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
     */
    public readonly cluster!: pulumi.Output<string | undefined>;
    /**
     * Column
     */
    public readonly columns!: pulumi.Output<outputs.TableColumn[] | undefined>;
    /**
     * Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * DB Name where the table will bellow
     */
    public readonly database!: pulumi.Output<string>;
    /**
     * Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
     */
    public readonly engine!: pulumi.Output<string>;
    /**
     * Engine params in case the engine type requires them
     */
    public readonly engineParams!: pulumi.Output<string[] | undefined>;
    /**
     * Index
     */
    public readonly indices!: pulumi.Output<outputs.TableIndex[] | undefined>;
    /**
     * Column Name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Order by columns to use as sorting key
     */
    public readonly orderBies!: pulumi.Output<string[] | undefined>;
    /**
     * Partition Key to split data
     */
    public readonly partitionBies!: pulumi.Output<outputs.TablePartitionBy[] | undefined>;
    /**
     * Table settings
     */
    public readonly settings!: pulumi.Output<{[key: string]: string} | undefined>;

    /**
     * Create a Table resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TableArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TableArgs | TableState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as TableState | undefined;
            resourceInputs["cluster"] = state ? state.cluster : undefined;
            resourceInputs["columns"] = state ? state.columns : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["database"] = state ? state.database : undefined;
            resourceInputs["engine"] = state ? state.engine : undefined;
            resourceInputs["engineParams"] = state ? state.engineParams : undefined;
            resourceInputs["indices"] = state ? state.indices : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["orderBies"] = state ? state.orderBies : undefined;
            resourceInputs["partitionBies"] = state ? state.partitionBies : undefined;
            resourceInputs["settings"] = state ? state.settings : undefined;
        } else {
            const args = argsOrState as TableArgs | undefined;
            if ((!args || args.database === undefined) && !opts.urn) {
                throw new Error("Missing required property 'database'");
            }
            if ((!args || args.engine === undefined) && !opts.urn) {
                throw new Error("Missing required property 'engine'");
            }
            resourceInputs["cluster"] = args ? args.cluster : undefined;
            resourceInputs["columns"] = args ? args.columns : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["database"] = args ? args.database : undefined;
            resourceInputs["engine"] = args ? args.engine : undefined;
            resourceInputs["engineParams"] = args ? args.engineParams : undefined;
            resourceInputs["indices"] = args ? args.indices : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["orderBies"] = args ? args.orderBies : undefined;
            resourceInputs["partitionBies"] = args ? args.partitionBies : undefined;
            resourceInputs["settings"] = args ? args.settings : undefined;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Table.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Table resources.
 */
export interface TableState {
    /**
     * Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
     */
    cluster?: pulumi.Input<string>;
    /**
     * Column
     */
    columns?: pulumi.Input<pulumi.Input<inputs.TableColumn>[]>;
    /**
     * Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
     */
    comment?: pulumi.Input<string>;
    /**
     * DB Name where the table will bellow
     */
    database?: pulumi.Input<string>;
    /**
     * Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
     */
    engine?: pulumi.Input<string>;
    /**
     * Engine params in case the engine type requires them
     */
    engineParams?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Index
     */
    indices?: pulumi.Input<pulumi.Input<inputs.TableIndex>[]>;
    /**
     * Column Name
     */
    name?: pulumi.Input<string>;
    /**
     * Order by columns to use as sorting key
     */
    orderBies?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Partition Key to split data
     */
    partitionBies?: pulumi.Input<pulumi.Input<inputs.TablePartitionBy>[]>;
    /**
     * Table settings
     */
    settings?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}

/**
 * The set of arguments for constructing a Table resource.
 */
export interface TableArgs {
    /**
     * Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
     */
    cluster?: pulumi.Input<string>;
    /**
     * Column
     */
    columns?: pulumi.Input<pulumi.Input<inputs.TableColumn>[]>;
    /**
     * Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
     */
    comment?: pulumi.Input<string>;
    /**
     * DB Name where the table will bellow
     */
    database: pulumi.Input<string>;
    /**
     * Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
     */
    engine: pulumi.Input<string>;
    /**
     * Engine params in case the engine type requires them
     */
    engineParams?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Index
     */
    indices?: pulumi.Input<pulumi.Input<inputs.TableIndex>[]>;
    /**
     * Column Name
     */
    name?: pulumi.Input<string>;
    /**
     * Order by columns to use as sorting key
     */
    orderBies?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Partition Key to split data
     */
    partitionBies?: pulumi.Input<pulumi.Input<inputs.TablePartitionBy>[]>;
    /**
     * Table settings
     */
    settings?: pulumi.Input<{[key: string]: pulumi.Input<string>}>;
}
