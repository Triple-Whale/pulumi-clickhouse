// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package clickhouse

import (
	"fmt"

	"github.com/Triple-Whale/pulumi-clickhouse/sdk/go/clickhouse/internal"
	"github.com/blang/semver"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "clickhouse:index/db:Db":
		r = &Db{}
	case "clickhouse:index/role:Role":
		r = &Role{}
	case "clickhouse:index/table:Table":
		r = &Table{}
	case "clickhouse:index/user:User":
		r = &User{}
	case "clickhouse:index/view:View":
		r = &View{}
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	err = ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return
}

type pkg struct {
	version semver.Version
}

func (p *pkg) Version() semver.Version {
	return p.version
}

func (p *pkg) ConstructProvider(ctx *pulumi.Context, name, typ, urn string) (pulumi.ProviderResource, error) {
	if typ != "pulumi:providers:clickhouse" {
		return nil, fmt.Errorf("unknown provider type: %s", typ)
	}

	r := &Provider{}
	err := ctx.RegisterResource(typ, name, nil, r, pulumi.URN_(urn))
	return r, err
}

func init() {
	version, err := internal.PkgVersion()
	if err != nil {
		version = semver.Version{Major: 1}
	}
	pulumi.RegisterResourceModule(
		"clickhouse",
		"index/db",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"clickhouse",
		"index/role",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"clickhouse",
		"index/table",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"clickhouse",
		"index/user",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"clickhouse",
		"index/view",
		&module{version},
	)
	pulumi.RegisterResourcePackage(
		"clickhouse",
		&pkg{version},
	)
}
