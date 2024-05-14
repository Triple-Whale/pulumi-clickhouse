// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Clickhouse.Inputs
{

    public sealed class TableColumnGetArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        [Input("defaultexpression")]
        public Input<string>? Defaultexpression { get; set; }

        [Input("defaultkind")]
        public Input<string>? Defaultkind { get; set; }

        /// <summary>
        /// Column Name
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        /// <summary>
        /// Column Type
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public TableColumnGetArgs()
        {
        }
        public static new TableColumnGetArgs Empty => new TableColumnGetArgs();
    }
}
