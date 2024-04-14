// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Clickhouse.Inputs
{

    public sealed class TablePartitionByArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Column to use as part of the partition key
        /// </summary>
        [Input("by", required: true)]
        public Input<string> By { get; set; } = null!;

        /// <summary>
        /// Partition function, could be empty or one of following: toYYYYMM, toYYYYMMDD or toYYYYMMDDhhmmss
        /// </summary>
        [Input("partitionFunction")]
        public Input<string>? PartitionFunction { get; set; }

        public TablePartitionByArgs()
        {
        }
        public static new TablePartitionByArgs Empty => new TablePartitionByArgs();
    }
}
