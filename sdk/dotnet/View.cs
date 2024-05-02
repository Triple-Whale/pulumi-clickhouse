// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Clickhouse
{
    [ClickhouseResourceType("clickhouse:index/view:View")]
    public partial class View : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Cluster Name
        /// </summary>
        [Output("cluster")]
        public Output<string?> Cluster { get; private set; } = null!;

        /// <summary>
        /// View comment, it will be codified in a json along with come metadata information (like cluster name in case of
        /// clustering)
        /// </summary>
        [Output("comment")]
        public Output<string?> Comment { get; private set; } = null!;

        /// <summary>
        /// DB Name where the view will bellow
        /// </summary>
        [Output("database")]
        public Output<string> Database { get; private set; } = null!;

        /// <summary>
        /// Is materialized view
        /// </summary>
        [Output("materialized")]
        public Output<bool?> Materialized { get; private set; } = null!;

        /// <summary>
        /// View Name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// View query
        /// </summary>
        [Output("query")]
        public Output<string> Query { get; private set; } = null!;

        /// <summary>
        /// For materialized view - destination table
        /// </summary>
        [Output("toTable")]
        public Output<string?> ToTable { get; private set; } = null!;


        /// <summary>
        /// Create a View resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public View(string name, ViewArgs args, CustomResourceOptions? options = null)
            : base("clickhouse:index/view:View", name, args ?? new ViewArgs(), MakeResourceOptions(options, ""))
        {
        }

        private View(string name, Input<string> id, ViewState? state = null, CustomResourceOptions? options = null)
            : base("clickhouse:index/view:View", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing View resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static View Get(string name, Input<string> id, ViewState? state = null, CustomResourceOptions? options = null)
        {
            return new View(name, id, state, options);
        }
    }

    public sealed class ViewArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster Name
        /// </summary>
        [Input("cluster")]
        public Input<string>? Cluster { get; set; }

        /// <summary>
        /// View comment, it will be codified in a json along with come metadata information (like cluster name in case of
        /// clustering)
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// DB Name where the view will bellow
        /// </summary>
        [Input("database", required: true)]
        public Input<string> Database { get; set; } = null!;

        /// <summary>
        /// Is materialized view
        /// </summary>
        [Input("materialized")]
        public Input<bool>? Materialized { get; set; }

        /// <summary>
        /// View Name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// View query
        /// </summary>
        [Input("query", required: true)]
        public Input<string> Query { get; set; } = null!;

        /// <summary>
        /// For materialized view - destination table
        /// </summary>
        [Input("toTable")]
        public Input<string>? ToTable { get; set; }

        public ViewArgs()
        {
        }
        public static new ViewArgs Empty => new ViewArgs();
    }

    public sealed class ViewState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Cluster Name
        /// </summary>
        [Input("cluster")]
        public Input<string>? Cluster { get; set; }

        /// <summary>
        /// View comment, it will be codified in a json along with come metadata information (like cluster name in case of
        /// clustering)
        /// </summary>
        [Input("comment")]
        public Input<string>? Comment { get; set; }

        /// <summary>
        /// DB Name where the view will bellow
        /// </summary>
        [Input("database")]
        public Input<string>? Database { get; set; }

        /// <summary>
        /// Is materialized view
        /// </summary>
        [Input("materialized")]
        public Input<bool>? Materialized { get; set; }

        /// <summary>
        /// View Name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// View query
        /// </summary>
        [Input("query")]
        public Input<string>? Query { get; set; }

        /// <summary>
        /// For materialized view - destination table
        /// </summary>
        [Input("toTable")]
        public Input<string>? ToTable { get; set; }

        public ViewState()
        {
        }
        public static new ViewState Empty => new ViewState();
    }
}