// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Clickhouse.Outputs
{

    [OutputType]
    public sealed class TablePartitionBy
    {
        /// <summary>
        /// Column to use as part of the partition key
        /// </summary>
        public readonly string By;
        public readonly string? Mod;
        /// <summary>
        /// Partition function, could be empty or one of following: toYYYYMM, toYYYYMMDD or toYYYYMMDDhhmmss
        /// </summary>
        public readonly string? PartitionFunction;

        [OutputConstructor]
        private TablePartitionBy(
            string by,

            string? mod,

            string? partitionFunction)
        {
            By = by;
            Mod = mod;
            PartitionFunction = partitionFunction;
        }
    }
}
