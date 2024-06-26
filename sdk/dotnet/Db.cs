// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Clickhouse
{
    /// <summary>
    /// Resource to handle clickhouse databases.
    /// </summary>
    [ClickhouseResourceType("clickhouse:index/db:Db")]
    public partial class Db : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Cluster name, not mandatory but should be provided if creating a db in a clustered server
        /// </summary>
        [Output("cluster")]
        public Output<string?> Cluster { get; private set; } = null!;

        /// <summary>
        /// Comment about the database
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// Database internal path
        /// </summary>
        [Output("dataPath")]
        public Output<string> DataPath { get; private set; } = null!;

        /// <summary>
        /// Database engine
        /// </summary>
        [Output("engine")]
        public Output<string> Engine { get; private set; } = null!;

        /// <summary>
        /// Database internal metadata path
        /// </summary>
        [Output("metadataPath")]
        public Output<string> MetadataPath { get; private set; } = null!;

        /// <summary>
        /// Database name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Database UUID
        /// </summary>
        [Output("uuid")]
        public Output<string> Uuid { get; private set; } = null!;


        /// <summary>
        /// Create a Db resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Db(string name, DbArgs? args = null, CustomResourceOptions? options = null)
            : base("clickhouse:index/db:Db", name, args ?? new DbArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Db(string name, Input<string> id, DbState? state = null, CustomResourceOptions? options = null)
            : base("clickhouse:index/db:Db", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "https://storage.googleapis.com/pulumi-shofifi/clickhouse",
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Db resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Db Get(string name, Input<string> id, DbState? state = null, CustomResourceOptions? options = null)
        {
            return new Db(name, id, state, options);
        }
    }

    public sealed class DbArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster name, not mandatory but should be provided if creating a db in a clustered server
        /// </summary>
        [Input("cluster")]
        public Input<string>? Cluster { get; set; }

        /// <summary>
        /// Comment about the database
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Database name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public DbArgs()
        {
        }
        public static new DbArgs Empty => new DbArgs();
    }

    public sealed class DbState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster name, not mandatory but should be provided if creating a db in a clustered server
        /// </summary>
        [Input("cluster")]
        public Input<string>? Cluster { get; set; }

        /// <summary>
        /// Comment about the database
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// Database internal path
        /// </summary>
        [Input("dataPath")]
        public Input<string>? DataPath { get; set; }

        /// <summary>
        /// Database engine
        /// </summary>
        [Input("engine")]
        public Input<string>? Engine { get; set; }

        /// <summary>
        /// Database internal metadata path
        /// </summary>
        [Input("metadataPath")]
        public Input<string>? MetadataPath { get; set; }

        /// <summary>
        /// Database name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Database UUID
        /// </summary>
        [Input("uuid")]
        public Input<string>? Uuid { get; set; }

        public DbState()
        {
        }
        public static new DbState Empty => new DbState();
    }
}
