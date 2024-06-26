// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

export interface TableColumn {
    /**
     * Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
     */
    comment?: pulumi.Input<string>;
    defaultExpression?: pulumi.Input<string>;
    defaultKind?: pulumi.Input<string>;
    /**
     * Column Name
     */
    name: pulumi.Input<string>;
    /**
     * Column Type
     */
    type: pulumi.Input<string>;
}

export interface TableIndex {
    expression: pulumi.Input<string>;
    granularity?: pulumi.Input<number>;
    /**
     * Column Name
     */
    name: pulumi.Input<string>;
    /**
     * Column Type
     */
    type: pulumi.Input<string>;
}

export interface TablePartitionBy {
    /**
     * Column to use as part of the partition key
     */
    by: pulumi.Input<string>;
    mod?: pulumi.Input<string>;
    /**
     * Partition function, could be empty or one of following: toYYYYMM, toYYYYMMDD or toYYYYMMDDhhmmss
     */
    partitionFunction?: pulumi.Input<string>;
}
