# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ViewArgs', 'View']

@pulumi.input_type
class ViewArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[str],
                 query: pulumi.Input[str],
                 cluster: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 materialized: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 to_table: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a View resource.
        :param pulumi.Input[str] database: DB Name where the view will bellow
        :param pulumi.Input[str] query: View query
        :param pulumi.Input[str] cluster: Cluster Name
        :param pulumi.Input[str] comment: View comment, it will be codified in a json along with come metadata information (like cluster name in case of
               clustering)
        :param pulumi.Input[bool] materialized: Is materialized view
        :param pulumi.Input[str] name: View Name
        :param pulumi.Input[str] to_table: For materialized view - destination table
        """
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "query", query)
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if materialized is not None:
            pulumi.set(__self__, "materialized", materialized)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if to_table is not None:
            pulumi.set(__self__, "to_table", to_table)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        DB Name where the view will bellow
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def query(self) -> pulumi.Input[str]:
        """
        View query
        """
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: pulumi.Input[str]):
        pulumi.set(self, "query", value)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster Name
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        View comment, it will be codified in a json along with come metadata information (like cluster name in case of
        clustering)
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def materialized(self) -> Optional[pulumi.Input[bool]]:
        """
        Is materialized view
        """
        return pulumi.get(self, "materialized")

    @materialized.setter
    def materialized(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "materialized", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        View Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="toTable")
    def to_table(self) -> Optional[pulumi.Input[str]]:
        """
        For materialized view - destination table
        """
        return pulumi.get(self, "to_table")

    @to_table.setter
    def to_table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "to_table", value)


@pulumi.input_type
class _ViewState:
    def __init__(__self__, *,
                 cluster: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 materialized: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 to_table: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering View resources.
        :param pulumi.Input[str] cluster: Cluster Name
        :param pulumi.Input[str] comment: View comment, it will be codified in a json along with come metadata information (like cluster name in case of
               clustering)
        :param pulumi.Input[str] database: DB Name where the view will bellow
        :param pulumi.Input[bool] materialized: Is materialized view
        :param pulumi.Input[str] name: View Name
        :param pulumi.Input[str] query: View query
        :param pulumi.Input[str] to_table: For materialized view - destination table
        """
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if database is not None:
            pulumi.set(__self__, "database", database)
        if materialized is not None:
            pulumi.set(__self__, "materialized", materialized)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if query is not None:
            pulumi.set(__self__, "query", query)
        if to_table is not None:
            pulumi.set(__self__, "to_table", to_table)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster Name
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        View comment, it will be codified in a json along with come metadata information (like cluster name in case of
        clustering)
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        DB Name where the view will bellow
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def materialized(self) -> Optional[pulumi.Input[bool]]:
        """
        Is materialized view
        """
        return pulumi.get(self, "materialized")

    @materialized.setter
    def materialized(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "materialized", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        View Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def query(self) -> Optional[pulumi.Input[str]]:
        """
        View query
        """
        return pulumi.get(self, "query")

    @query.setter
    def query(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "query", value)

    @property
    @pulumi.getter(name="toTable")
    def to_table(self) -> Optional[pulumi.Input[str]]:
        """
        For materialized view - destination table
        """
        return pulumi.get(self, "to_table")

    @to_table.setter
    def to_table(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "to_table", value)


class View(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 materialized: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 to_table: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a View resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: Cluster Name
        :param pulumi.Input[str] comment: View comment, it will be codified in a json along with come metadata information (like cluster name in case of
               clustering)
        :param pulumi.Input[str] database: DB Name where the view will bellow
        :param pulumi.Input[bool] materialized: Is materialized view
        :param pulumi.Input[str] name: View Name
        :param pulumi.Input[str] query: View query
        :param pulumi.Input[str] to_table: For materialized view - destination table
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ViewArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a View resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ViewArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ViewArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 materialized: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 query: Optional[pulumi.Input[str]] = None,
                 to_table: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ViewArgs.__new__(ViewArgs)

            __props__.__dict__["cluster"] = cluster
            __props__.__dict__["comment"] = comment
            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            __props__.__dict__["materialized"] = materialized
            __props__.__dict__["name"] = name
            if query is None and not opts.urn:
                raise TypeError("Missing required property 'query'")
            __props__.__dict__["query"] = query
            __props__.__dict__["to_table"] = to_table
        super(View, __self__).__init__(
            'clickhouse:index/view:View',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster: Optional[pulumi.Input[str]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            database: Optional[pulumi.Input[str]] = None,
            materialized: Optional[pulumi.Input[bool]] = None,
            name: Optional[pulumi.Input[str]] = None,
            query: Optional[pulumi.Input[str]] = None,
            to_table: Optional[pulumi.Input[str]] = None) -> 'View':
        """
        Get an existing View resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: Cluster Name
        :param pulumi.Input[str] comment: View comment, it will be codified in a json along with come metadata information (like cluster name in case of
               clustering)
        :param pulumi.Input[str] database: DB Name where the view will bellow
        :param pulumi.Input[bool] materialized: Is materialized view
        :param pulumi.Input[str] name: View Name
        :param pulumi.Input[str] query: View query
        :param pulumi.Input[str] to_table: For materialized view - destination table
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ViewState.__new__(_ViewState)

        __props__.__dict__["cluster"] = cluster
        __props__.__dict__["comment"] = comment
        __props__.__dict__["database"] = database
        __props__.__dict__["materialized"] = materialized
        __props__.__dict__["name"] = name
        __props__.__dict__["query"] = query
        __props__.__dict__["to_table"] = to_table
        return View(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[Optional[str]]:
        """
        Cluster Name
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        View comment, it will be codified in a json along with come metadata information (like cluster name in case of
        clustering)
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        DB Name where the view will bellow
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def materialized(self) -> pulumi.Output[Optional[bool]]:
        """
        Is materialized view
        """
        return pulumi.get(self, "materialized")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        View Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def query(self) -> pulumi.Output[str]:
        """
        View query
        """
        return pulumi.get(self, "query")

    @property
    @pulumi.getter(name="toTable")
    def to_table(self) -> pulumi.Output[Optional[str]]:
        """
        For materialized view - destination table
        """
        return pulumi.get(self, "to_table")
