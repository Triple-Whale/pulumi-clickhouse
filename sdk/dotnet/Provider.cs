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
    /// The provider type for the clickhouse package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// </summary>
    [ClickhouseResourceType("pulumi:providers:clickhouse")]
    public partial class Provider : global::Pulumi.ProviderResource
    {
        /// <summary>
        /// Default cluster, if provided will be used when no cluster is provided
        /// </summary>
        [Output("defaultCluster")]
        public Output<string?> DefaultCluster { get; private set; } = null!;

        /// <summary>
        /// Clickhouse server url
        /// </summary>
        [Output("host")]
        public Output<string> Host { get; private set; } = null!;

        /// <summary>
        /// Clickhouse user password with admin privileges
        /// </summary>
        [Output("password")]
        public Output<string?> Password { get; private set; } = null!;

        /// <summary>
        /// Clickhouse username with admin privileges
        /// </summary>
        [Output("username")]
        public Output<string?> Username { get; private set; } = null!;


        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs args, CustomResourceOptions? options = null)
            : base("clickhouse", name, args ?? new ProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                AdditionalSecretOutputs =
                {
                    "host",
                    "password",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Default cluster, if provided will be used when no cluster is provided
        /// </summary>
        [Input("defaultCluster")]
        public Input<string>? DefaultCluster { get; set; }

        [Input("host", required: true)]
        private Input<string>? _host;

        /// <summary>
        /// Clickhouse server url
        /// </summary>
        public Input<string>? Host
        {
            get => _host;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _host = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        [Input("password")]
        private Input<string>? _password;

        /// <summary>
        /// Clickhouse user password with admin privileges
        /// </summary>
        public Input<string>? Password
        {
            get => _password;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _password = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        /// <summary>
        /// Clickhouse server native protocol port (TCP)
        /// </summary>
        [Input("port", required: true, json: true)]
        public Input<int> Port { get; set; } = null!;

        /// <summary>
        /// Clickhouse secure connection
        /// </summary>
        [Input("secure", json: true)]
        public Input<bool>? Secure { get; set; }

        /// <summary>
        /// Clickhouse username with admin privileges
        /// </summary>
        [Input("username")]
        public Input<string>? Username { get; set; }

        public ProviderArgs()
        {
        }
        public static new ProviderArgs Empty => new ProviderArgs();
    }
}
