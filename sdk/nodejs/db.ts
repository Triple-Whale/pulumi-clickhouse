// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Resource to handle clickhouse databases.
 */
export class Db extends pulumi.CustomResource {
    /**
     * Get an existing Db resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DbState, opts?: pulumi.CustomResourceOptions): Db {
        return new Db(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'clickhouse:index/db:Db';

    /**
     * Returns true if the given object is an instance of Db.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Db {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Db.__pulumiType;
    }

    /**
     * Cluster name, not mandatory but should be provided if creating a db in a clustered server
     */
    public readonly cluster!: pulumi.Output<string | undefined>;
    /**
     * Comment about the database
     */
    public readonly comment!: pulumi.Output<string | undefined>;
    /**
     * Database internal path
     */
    public /*out*/ readonly dataPath!: pulumi.Output<string>;
    /**
     * Database engine
     */
    public /*out*/ readonly engine!: pulumi.Output<string>;
    /**
     * Database internal metadata path
     */
    public /*out*/ readonly metadataPath!: pulumi.Output<string>;
    /**
     * Database name
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Database UUID
     */
    public /*out*/ readonly uuid!: pulumi.Output<string>;

    /**
     * Create a Db resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: DbArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DbArgs | DbState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as DbState | undefined;
            resourceInputs["cluster"] = state ? state.cluster : undefined;
            resourceInputs["comment"] = state ? state.comment : undefined;
            resourceInputs["dataPath"] = state ? state.dataPath : undefined;
            resourceInputs["engine"] = state ? state.engine : undefined;
            resourceInputs["metadataPath"] = state ? state.metadataPath : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["uuid"] = state ? state.uuid : undefined;
        } else {
            const args = argsOrState as DbArgs | undefined;
            resourceInputs["cluster"] = args ? args.cluster : undefined;
            resourceInputs["comment"] = args ? args.comment : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["dataPath"] = undefined /*out*/;
            resourceInputs["engine"] = undefined /*out*/;
            resourceInputs["metadataPath"] = undefined /*out*/;
            resourceInputs["uuid"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Db.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Db resources.
 */
export interface DbState {
    /**
     * Cluster name, not mandatory but should be provided if creating a db in a clustered server
     */
    cluster?: pulumi.Input<string>;
    /**
     * Comment about the database
     */
    comment?: pulumi.Input<string>;
    /**
     * Database internal path
     */
    dataPath?: pulumi.Input<string>;
    /**
     * Database engine
     */
    engine?: pulumi.Input<string>;
    /**
     * Database internal metadata path
     */
    metadataPath?: pulumi.Input<string>;
    /**
     * Database name
     */
    name?: pulumi.Input<string>;
    /**
     * Database UUID
     */
    uuid?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Db resource.
 */
export interface DbArgs {
    /**
     * Cluster name, not mandatory but should be provided if creating a db in a clustered server
     */
    cluster?: pulumi.Input<string>;
    /**
     * Comment about the database
     */
    comment?: pulumi.Input<string>;
    /**
     * Database name
     */
    name?: pulumi.Input<string>;
}
