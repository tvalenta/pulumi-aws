// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as fabric from "@pulumi/pulumi-fabric";

/**
 * Provides a Kinesis Firehose Delivery Stream resource. Amazon Kinesis Firehose is a fully managed, elastic service to easily deliver real-time data streams to destinations such as Amazon S3 and Amazon Redshift.
 * 
 * For more details, see the [Amazon Kinesis Firehose Documentation][1].
 */
export class FirehoseDeliveryStream extends fabric.Resource {
    /**
     * The Amazon Resource Name (ARN) specifying the Stream
     */
    public readonly arn: fabric.Computed<string>;
    /**
     * This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, and `elasticsearch`.
     */
    public readonly destination: fabric.Computed<string>;
    public readonly destinationId: fabric.Computed<string>;
    public readonly elasticsearchConfiguration?: fabric.Computed<{ bufferingInterval?: number, bufferingSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }[], domainArn: string, indexName: string, indexRotationPeriod?: string, retryDuration?: number, roleArn: string, s3BackupMode?: string, typeName?: string }[]>;
    /**
     * Enhanced configuration options for the s3 destination. More details are given below.
     */
    public readonly extendedS3Configuration?: fabric.Computed<{ bucketArn: string, bufferInterval?: number, bufferSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }[], compressionFormat?: string, kmsKeyArn?: string, prefix?: string, processingConfiguration?: { enabled?: boolean, processors?: { parameters?: { parameterName: string, parameterValue: string }[], type: string }[] }[], roleArn: string }[]>;
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    public readonly name: fabric.Computed<string>;
    /**
     * Configuration options if redshift is the destination.
     * Using `redshift_configuration` requires the user to also specify a
     * `s3_configuration` block. More details are given below.
     */
    public readonly redshiftConfiguration?: fabric.Computed<{ cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }[], clusterJdbcurl: string, copyOptions?: string, dataTableColumns?: string, dataTableName: string, password: string, retryDuration?: number, roleArn: string, username: string }[]>;
    /**
     * Configuration options for the s3 destination (or the intermediate bucket if the destination
     * is redshift). More details are given below.
     */
    public readonly s3Configuration?: fabric.Computed<{ bucketArn: string, bufferInterval?: number, bufferSize?: number, cloudwatchLoggingOptions: { enabled?: boolean, logGroupName?: string, logStreamName?: string }[], compressionFormat?: string, kmsKeyArn?: string, prefix?: string, roleArn: string }[]>;
    public readonly versionId: fabric.Computed<string>;

    /**
     * Create a FirehoseDeliveryStream resource with the given unique name, arguments and optional additional
     * resource dependencies.
     *
     * @param urnName A _unique_ name for this FirehoseDeliveryStream instance
     * @param args A collection of arguments for creating this FirehoseDeliveryStream intance
     * @param dependsOn A optional array of additional resources this intance depends on
     */
    constructor(urnName: string, args: FirehoseDeliveryStreamArgs, dependsOn?: fabric.Resource[]) {
        if (args.destination === undefined) {
            throw new Error("Missing required property 'destination'");
        }
        super("aws:kinesis/firehoseDeliveryStream:FirehoseDeliveryStream", urnName, {
            "arn": args.arn,
            "destination": args.destination,
            "destinationId": args.destinationId,
            "elasticsearchConfiguration": args.elasticsearchConfiguration,
            "extendedS3Configuration": args.extendedS3Configuration,
            "name": args.name,
            "redshiftConfiguration": args.redshiftConfiguration,
            "s3Configuration": args.s3Configuration,
            "versionId": args.versionId,
        }, dependsOn);
    }
}

/**
 * The set of arguments for constructing a FirehoseDeliveryStream resource.
 */
export interface FirehoseDeliveryStreamArgs {
    readonly arn?: fabric.ComputedValue<string>;
    /**
     * This is the destination to where the data is delivered. The only options are `s3` (Deprecated, use `extended_s3` instead), `extended_s3`, `redshift`, and `elasticsearch`.
     */
    readonly destination: fabric.ComputedValue<string>;
    readonly destinationId?: fabric.ComputedValue<string>;
    readonly elasticsearchConfiguration?: fabric.ComputedValue<{ bufferingInterval?: fabric.ComputedValue<number>, bufferingSize?: fabric.ComputedValue<number>, cloudwatchLoggingOptions?: fabric.ComputedValue<{ enabled?: fabric.ComputedValue<boolean>, logGroupName?: fabric.ComputedValue<string>, logStreamName?: fabric.ComputedValue<string> }>[], domainArn: fabric.ComputedValue<string>, indexName: fabric.ComputedValue<string>, indexRotationPeriod?: fabric.ComputedValue<string>, retryDuration?: fabric.ComputedValue<number>, roleArn: fabric.ComputedValue<string>, s3BackupMode?: fabric.ComputedValue<string>, typeName?: fabric.ComputedValue<string> }>[];
    /**
     * Enhanced configuration options for the s3 destination. More details are given below.
     */
    readonly extendedS3Configuration?: fabric.ComputedValue<{ bucketArn: fabric.ComputedValue<string>, bufferInterval?: fabric.ComputedValue<number>, bufferSize?: fabric.ComputedValue<number>, cloudwatchLoggingOptions?: fabric.ComputedValue<{ enabled?: fabric.ComputedValue<boolean>, logGroupName?: fabric.ComputedValue<string>, logStreamName?: fabric.ComputedValue<string> }>[], compressionFormat?: fabric.ComputedValue<string>, kmsKeyArn?: fabric.ComputedValue<string>, prefix?: fabric.ComputedValue<string>, processingConfiguration?: fabric.ComputedValue<{ enabled?: fabric.ComputedValue<boolean>, processors?: fabric.ComputedValue<{ parameters?: fabric.ComputedValue<{ parameterName: fabric.ComputedValue<string>, parameterValue: fabric.ComputedValue<string> }>[], type: fabric.ComputedValue<string> }>[] }>[], roleArn: fabric.ComputedValue<string> }>[];
    /**
     * A name to identify the stream. This is unique to the
     * AWS account and region the Stream is created in.
     */
    readonly name?: fabric.ComputedValue<string>;
    /**
     * Configuration options if redshift is the destination.
     * Using `redshift_configuration` requires the user to also specify a
     * `s3_configuration` block. More details are given below.
     */
    readonly redshiftConfiguration?: fabric.ComputedValue<{ cloudwatchLoggingOptions?: fabric.ComputedValue<{ enabled?: fabric.ComputedValue<boolean>, logGroupName?: fabric.ComputedValue<string>, logStreamName?: fabric.ComputedValue<string> }>[], clusterJdbcurl: fabric.ComputedValue<string>, copyOptions?: fabric.ComputedValue<string>, dataTableColumns?: fabric.ComputedValue<string>, dataTableName: fabric.ComputedValue<string>, password: fabric.ComputedValue<string>, retryDuration?: fabric.ComputedValue<number>, roleArn: fabric.ComputedValue<string>, username: fabric.ComputedValue<string> }>[];
    /**
     * Configuration options for the s3 destination (or the intermediate bucket if the destination
     * is redshift). More details are given below.
     */
    readonly s3Configuration?: fabric.ComputedValue<{ bucketArn: fabric.ComputedValue<string>, bufferInterval?: fabric.ComputedValue<number>, bufferSize?: fabric.ComputedValue<number>, cloudwatchLoggingOptions?: fabric.ComputedValue<{ enabled?: fabric.ComputedValue<boolean>, logGroupName?: fabric.ComputedValue<string>, logStreamName?: fabric.ComputedValue<string> }>[], compressionFormat?: fabric.ComputedValue<string>, kmsKeyArn?: fabric.ComputedValue<string>, prefix?: fabric.ComputedValue<string>, roleArn: fabric.ComputedValue<string> }>[];
    readonly versionId?: fabric.ComputedValue<string>;
}

