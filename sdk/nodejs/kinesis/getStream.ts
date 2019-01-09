// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this data source to get information about a Kinesis Stream for use in other
 * resources.
 * 
 * For more details, see the [Amazon Kinesis Documentation][1].
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_kinesis_stream_stream = pulumi.output(aws.kinesis.getStream({
 *     name: "stream-name",
 * }));
 * ```
 */
export function getStream(args: GetStreamArgs, opts?: pulumi.InvokeOptions): Promise<GetStreamResult> {
    return pulumi.runtime.invoke("aws:kinesis/getStream:getStream", {
        "name": args.name,
    }, opts);
}

/**
 * A collection of arguments for invoking getStream.
 */
export interface GetStreamArgs {
    /**
     * The name of the Kinesis Stream.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getStream.
 */
export interface GetStreamResult {
    /**
     * The Amazon Resource Name (ARN) of the Kinesis Stream (same as id).
     */
    readonly arn: string;
    /**
     * The list of shard ids in the CLOSED state. See [Shard State][2] for more.
     */
    readonly closedShards: string[];
    /**
     * The approximate UNIX timestamp that the stream was created.
     */
    readonly creationTimestamp: number;
    /**
     * The list of shard ids in the OPEN state. See [Shard State][2] for more.
     */
    readonly openShards: string[];
    /**
     * Length of time (in hours) data records are accessible after they are added to the stream.
     */
    readonly retentionPeriod: number;
    /**
     * A list of shard-level CloudWatch metrics which are enabled for the stream. See [Monitoring with CloudWatch][3] for more.
     */
    readonly shardLevelMetrics: string[];
    /**
     * The current status of the stream. The stream status is one of CREATING, DELETING, ACTIVE, or UPDATING.
     */
    readonly status: string;
    /**
     * A mapping of tags to assigned to the stream.
     */
    readonly tags: {[key: string]: any};
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
