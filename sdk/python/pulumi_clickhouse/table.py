# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['TableArgs', 'Table']

@pulumi.input_type
class TableArgs:
    def __init__(__self__, *,
                 database: pulumi.Input[str],
                 engine: pulumi.Input[str],
                 cluster: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 engine_params: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 indices: Optional[pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 partition_bies: Optional[pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]]] = None,
                 settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Table resource.
        :param pulumi.Input[str] database: DB Name where the table will bellow
        :param pulumi.Input[str] engine: Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        :param pulumi.Input[str] cluster: Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        :param pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]] columns: Column
        :param pulumi.Input[str] comment: Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] engine_params: Engine params in case the engine type requires them
        :param pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]] indices: Index
        :param pulumi.Input[str] name: Column Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] order_bies: Order by columns to use as sorting key
        :param pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]] partition_bies: Partition Key to split data
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] settings: Table settings
        """
        pulumi.set(__self__, "database", database)
        pulumi.set(__self__, "engine", engine)
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if engine_params is not None:
            pulumi.set(__self__, "engine_params", engine_params)
        if indices is not None:
            pulumi.set(__self__, "indices", indices)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order_bies is not None:
            pulumi.set(__self__, "order_bies", order_bies)
        if partition_bies is not None:
            pulumi.set(__self__, "partition_bies", partition_bies)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter
    def database(self) -> pulumi.Input[str]:
        """
        DB Name where the table will bellow
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: pulumi.Input[str]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Input[str]:
        """
        Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: pulumi.Input[str]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]:
        """
        Column
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter(name="engineParams")
    def engine_params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Engine params in case the engine type requires them
        """
        return pulumi.get(self, "engine_params")

    @engine_params.setter
    def engine_params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "engine_params", value)

    @property
    @pulumi.getter
    def indices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]]]:
        """
        Index
        """
        return pulumi.get(self, "indices")

    @indices.setter
    def indices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]]]):
        pulumi.set(self, "indices", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Column Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orderBies")
    def order_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Order by columns to use as sorting key
        """
        return pulumi.get(self, "order_bies")

    @order_bies.setter
    def order_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "order_bies", value)

    @property
    @pulumi.getter(name="partitionBies")
    def partition_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]]]:
        """
        Partition Key to split data
        """
        return pulumi.get(self, "partition_bies")

    @partition_bies.setter
    def partition_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]]]):
        pulumi.set(self, "partition_bies", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Table settings
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "settings", value)


@pulumi.input_type
class _TableState:
    def __init__(__self__, *,
                 cluster: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_params: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 indices: Optional[pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 partition_bies: Optional[pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]]] = None,
                 settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        Input properties used for looking up and filtering Table resources.
        :param pulumi.Input[str] cluster: Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        :param pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]] columns: Column
        :param pulumi.Input[str] comment: Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        :param pulumi.Input[str] database: DB Name where the table will bellow
        :param pulumi.Input[str] engine: Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] engine_params: Engine params in case the engine type requires them
        :param pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]] indices: Index
        :param pulumi.Input[str] name: Column Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] order_bies: Order by columns to use as sorting key
        :param pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]] partition_bies: Partition Key to split data
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] settings: Table settings
        """
        if cluster is not None:
            pulumi.set(__self__, "cluster", cluster)
        if columns is not None:
            pulumi.set(__self__, "columns", columns)
        if comment is not None:
            pulumi.set(__self__, "comment", comment)
        if database is not None:
            pulumi.set(__self__, "database", database)
        if engine is not None:
            pulumi.set(__self__, "engine", engine)
        if engine_params is not None:
            pulumi.set(__self__, "engine_params", engine_params)
        if indices is not None:
            pulumi.set(__self__, "indices", indices)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order_bies is not None:
            pulumi.set(__self__, "order_bies", order_bies)
        if partition_bies is not None:
            pulumi.set(__self__, "partition_bies", partition_bies)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)

    @property
    @pulumi.getter
    def cluster(self) -> Optional[pulumi.Input[str]]:
        """
        Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        """
        return pulumi.get(self, "cluster")

    @cluster.setter
    def cluster(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster", value)

    @property
    @pulumi.getter
    def columns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]:
        """
        Column
        """
        return pulumi.get(self, "columns")

    @columns.setter
    def columns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableColumnArgs']]]]):
        pulumi.set(self, "columns", value)

    @property
    @pulumi.getter
    def comment(self) -> Optional[pulumi.Input[str]]:
        """
        Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        """
        return pulumi.get(self, "comment")

    @comment.setter
    def comment(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "comment", value)

    @property
    @pulumi.getter
    def database(self) -> Optional[pulumi.Input[str]]:
        """
        DB Name where the table will bellow
        """
        return pulumi.get(self, "database")

    @database.setter
    def database(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database", value)

    @property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[str]]:
        """
        Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        """
        return pulumi.get(self, "engine")

    @engine.setter
    def engine(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "engine", value)

    @property
    @pulumi.getter(name="engineParams")
    def engine_params(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Engine params in case the engine type requires them
        """
        return pulumi.get(self, "engine_params")

    @engine_params.setter
    def engine_params(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "engine_params", value)

    @property
    @pulumi.getter
    def indices(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]]]:
        """
        Index
        """
        return pulumi.get(self, "indices")

    @indices.setter
    def indices(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TableIndexArgs']]]]):
        pulumi.set(self, "indices", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Column Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="orderBies")
    def order_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Order by columns to use as sorting key
        """
        return pulumi.get(self, "order_bies")

    @order_bies.setter
    def order_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "order_bies", value)

    @property
    @pulumi.getter(name="partitionBies")
    def partition_bies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]]]:
        """
        Partition Key to split data
        """
        return pulumi.get(self, "partition_bies")

    @partition_bies.setter
    def partition_bies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TablePartitionByArgs']]]]):
        pulumi.set(self, "partition_bies", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Table settings
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "settings", value)


class Table(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_params: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 indices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableIndexArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 partition_bies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePartitionByArgs']]]]] = None,
                 settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Resource to manage tables

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]] columns: Column
        :param pulumi.Input[str] comment: Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        :param pulumi.Input[str] database: DB Name where the table will bellow
        :param pulumi.Input[str] engine: Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] engine_params: Engine params in case the engine type requires them
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableIndexArgs']]]] indices: Index
        :param pulumi.Input[str] name: Column Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] order_bies: Order by columns to use as sorting key
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePartitionByArgs']]]] partition_bies: Partition Key to split data
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] settings: Table settings
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: TableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Resource to manage tables

        :param str resource_name: The name of the resource.
        :param TableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(TableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster: Optional[pulumi.Input[str]] = None,
                 columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
                 comment: Optional[pulumi.Input[str]] = None,
                 database: Optional[pulumi.Input[str]] = None,
                 engine: Optional[pulumi.Input[str]] = None,
                 engine_params: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 indices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableIndexArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 order_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 partition_bies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePartitionByArgs']]]]] = None,
                 settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = TableArgs.__new__(TableArgs)

            __props__.__dict__["cluster"] = cluster
            __props__.__dict__["columns"] = columns
            __props__.__dict__["comment"] = comment
            if database is None and not opts.urn:
                raise TypeError("Missing required property 'database'")
            __props__.__dict__["database"] = database
            if engine is None and not opts.urn:
                raise TypeError("Missing required property 'engine'")
            __props__.__dict__["engine"] = engine
            __props__.__dict__["engine_params"] = engine_params
            __props__.__dict__["indices"] = indices
            __props__.__dict__["name"] = name
            __props__.__dict__["order_bies"] = order_bies
            __props__.__dict__["partition_bies"] = partition_bies
            __props__.__dict__["settings"] = settings
        super(Table, __self__).__init__(
            'clickhouse:index/table:Table',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster: Optional[pulumi.Input[str]] = None,
            columns: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]]] = None,
            comment: Optional[pulumi.Input[str]] = None,
            database: Optional[pulumi.Input[str]] = None,
            engine: Optional[pulumi.Input[str]] = None,
            engine_params: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            indices: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableIndexArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            order_bies: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            partition_bies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePartitionByArgs']]]]] = None,
            settings: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None) -> 'Table':
        """
        Get an existing Table resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster: Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableColumnArgs']]]] columns: Column
        :param pulumi.Input[str] comment: Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        :param pulumi.Input[str] database: DB Name where the table will bellow
        :param pulumi.Input[str] engine: Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        :param pulumi.Input[Sequence[pulumi.Input[str]]] engine_params: Engine params in case the engine type requires them
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TableIndexArgs']]]] indices: Index
        :param pulumi.Input[str] name: Column Name
        :param pulumi.Input[Sequence[pulumi.Input[str]]] order_bies: Order by columns to use as sorting key
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['TablePartitionByArgs']]]] partition_bies: Partition Key to split data
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] settings: Table settings
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _TableState.__new__(_TableState)

        __props__.__dict__["cluster"] = cluster
        __props__.__dict__["columns"] = columns
        __props__.__dict__["comment"] = comment
        __props__.__dict__["database"] = database
        __props__.__dict__["engine"] = engine
        __props__.__dict__["engine_params"] = engine_params
        __props__.__dict__["indices"] = indices
        __props__.__dict__["name"] = name
        __props__.__dict__["order_bies"] = order_bies
        __props__.__dict__["partition_bies"] = partition_bies
        __props__.__dict__["settings"] = settings
        return Table(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cluster(self) -> pulumi.Output[Optional[str]]:
        """
        Cluster Name, it is required for Replicated or Distributed tables and forbidden in other case
        """
        return pulumi.get(self, "cluster")

    @property
    @pulumi.getter
    def columns(self) -> pulumi.Output[Optional[Sequence['outputs.TableColumn']]]:
        """
        Column
        """
        return pulumi.get(self, "columns")

    @property
    @pulumi.getter
    def comment(self) -> pulumi.Output[Optional[str]]:
        """
        Database comment, it will be codified in a json along with come metadata information (like cluster name in case of clustering)
        """
        return pulumi.get(self, "comment")

    @property
    @pulumi.getter
    def database(self) -> pulumi.Output[str]:
        """
        DB Name where the table will bellow
        """
        return pulumi.get(self, "database")

    @property
    @pulumi.getter
    def engine(self) -> pulumi.Output[str]:
        """
        Table engine type (Supported types so far: Distributed, ReplicatedReplacingMergeTree, ReplacingMergeTree)
        """
        return pulumi.get(self, "engine")

    @property
    @pulumi.getter(name="engineParams")
    def engine_params(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Engine params in case the engine type requires them
        """
        return pulumi.get(self, "engine_params")

    @property
    @pulumi.getter
    def indices(self) -> pulumi.Output[Optional[Sequence['outputs.TableIndex']]]:
        """
        Index
        """
        return pulumi.get(self, "indices")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Column Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="orderBies")
    def order_bies(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Order by columns to use as sorting key
        """
        return pulumi.get(self, "order_bies")

    @property
    @pulumi.getter(name="partitionBies")
    def partition_bies(self) -> pulumi.Output[Optional[Sequence['outputs.TablePartitionBy']]]:
        """
        Partition Key to split data
        """
        return pulumi.get(self, "partition_bies")

    @property
    @pulumi.getter
    def settings(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Table settings
        """
        return pulumi.get(self, "settings")

