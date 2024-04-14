# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ProviderArgs', 'Provider']

@pulumi.input_type
class ProviderArgs:
    def __init__(__self__, *,
                 host: pulumi.Input[str],
                 port: pulumi.Input[int],
                 default_cluster: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 secure: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Provider resource.
        :param pulumi.Input[str] host: Clickhouse server url
        :param pulumi.Input[int] port: Clickhouse server native protocol port (TCP)
        :param pulumi.Input[str] default_cluster: Default cluster, if provided will be used when no cluster is provided
        :param pulumi.Input[str] password: Clickhouse user password with admin privileges
        :param pulumi.Input[bool] secure: Clickhouse secure connection
        :param pulumi.Input[str] username: Clickhouse username with admin privileges
        """
        pulumi.set(__self__, "host", host)
        pulumi.set(__self__, "port", port)
        if default_cluster is not None:
            pulumi.set(__self__, "default_cluster", default_cluster)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if secure is not None:
            pulumi.set(__self__, "secure", secure)
        if username is not None:
            pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        Clickhouse server url
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def port(self) -> pulumi.Input[int]:
        """
        Clickhouse server native protocol port (TCP)
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: pulumi.Input[int]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter(name="defaultCluster")
    def default_cluster(self) -> Optional[pulumi.Input[str]]:
        """
        Default cluster, if provided will be used when no cluster is provided
        """
        return pulumi.get(self, "default_cluster")

    @default_cluster.setter
    def default_cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_cluster", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Clickhouse user password with admin privileges
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter
    def secure(self) -> Optional[pulumi.Input[bool]]:
        """
        Clickhouse secure connection
        """
        return pulumi.get(self, "secure")

    @secure.setter
    def secure(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "secure", value)

    @property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[str]]:
        """
        Clickhouse username with admin privileges
        """
        return pulumi.get(self, "username")

    @username.setter
    def username(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "username", value)


class Provider(pulumi.ProviderResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_cluster: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 secure: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The provider type for the clickhouse package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_cluster: Default cluster, if provided will be used when no cluster is provided
        :param pulumi.Input[str] host: Clickhouse server url
        :param pulumi.Input[str] password: Clickhouse user password with admin privileges
        :param pulumi.Input[int] port: Clickhouse server native protocol port (TCP)
        :param pulumi.Input[bool] secure: Clickhouse secure connection
        :param pulumi.Input[str] username: Clickhouse username with admin privileges
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProviderArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The provider type for the clickhouse package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.

        :param str resource_name: The name of the resource.
        :param ProviderArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProviderArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_cluster: Optional[pulumi.Input[str]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 secure: Optional[pulumi.Input[bool]] = None,
                 username: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProviderArgs.__new__(ProviderArgs)

            __props__.__dict__["default_cluster"] = default_cluster
            if host is None and not opts.urn:
                raise TypeError("Missing required property 'host'")
            __props__.__dict__["host"] = None if host is None else pulumi.Output.secret(host)
            __props__.__dict__["password"] = None if password is None else pulumi.Output.secret(password)
            if port is None and not opts.urn:
                raise TypeError("Missing required property 'port'")
            __props__.__dict__["port"] = pulumi.Output.from_input(port).apply(pulumi.runtime.to_json) if port is not None else None
            __props__.__dict__["secure"] = pulumi.Output.from_input(secure).apply(pulumi.runtime.to_json) if secure is not None else None
            __props__.__dict__["username"] = username
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["host", "password"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(Provider, __self__).__init__(
            'clickhouse',
            resource_name,
            __props__,
            opts)

    @property
    @pulumi.getter(name="defaultCluster")
    def default_cluster(self) -> pulumi.Output[Optional[str]]:
        """
        Default cluster, if provided will be used when no cluster is provided
        """
        return pulumi.get(self, "default_cluster")

    @property
    @pulumi.getter
    def host(self) -> pulumi.Output[str]:
        """
        Clickhouse server url
        """
        return pulumi.get(self, "host")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Clickhouse user password with admin privileges
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> pulumi.Output[Optional[str]]:
        """
        Clickhouse username with admin privileges
        """
        return pulumi.get(self, "username")

