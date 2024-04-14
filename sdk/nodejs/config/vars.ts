// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("clickhouse");

/**
 * Default cluster, if provided will be used when no cluster is provided
 */
export declare const defaultCluster: string | undefined;
Object.defineProperty(exports, "defaultCluster", {
    get() {
        return __config.get("defaultCluster");
    },
    enumerable: true,
});

/**
 * Clickhouse server url
 */
export declare const host: string | undefined;
Object.defineProperty(exports, "host", {
    get() {
        return __config.get("host");
    },
    enumerable: true,
});

/**
 * Clickhouse user password with admin privileges
 */
export declare const password: string | undefined;
Object.defineProperty(exports, "password", {
    get() {
        return __config.get("password");
    },
    enumerable: true,
});

/**
 * Clickhouse server native protocol port (TCP)
 */
export declare const port: number | undefined;
Object.defineProperty(exports, "port", {
    get() {
        return __config.getObject<number>("port");
    },
    enumerable: true,
});

/**
 * Clickhouse secure connection
 */
export declare const secure: boolean | undefined;
Object.defineProperty(exports, "secure", {
    get() {
        return __config.getObject<boolean>("secure");
    },
    enumerable: true,
});

/**
 * Clickhouse username with admin privileges
 */
export declare const username: string | undefined;
Object.defineProperty(exports, "username", {
    get() {
        return __config.get("username");
    },
    enumerable: true,
});

