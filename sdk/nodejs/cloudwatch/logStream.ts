// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides a CloudWatch Log Stream resource.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_cloudwatch_log_group_yada = new aws.cloudwatch.LogGroup("yada", {
 *     name: "Yada",
 * });
 * const aws_cloudwatch_log_stream_foo = new aws.cloudwatch.LogStream("foo", {
 *     logGroupName: aws_cloudwatch_log_group_yada.name,
 *     name: "SampleLogStream1234",
 * });
 * ```
 */
export class LogStream extends pulumi.CustomResource {
    /**
     * Get an existing LogStream resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LogStreamState, opts?: pulumi.CustomResourceOptions): LogStream {
        return new LogStream(name, <any>state, { ...opts, id: id });
    }

    /**
     * The Amazon Resource Name (ARN) specifying the log stream.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The name of the log group under which the log stream is to be created.
     */
    public readonly logGroupName: pulumi.Output<string>;
    /**
     * The name of the log stream. Must not be longer than 512 characters and must not contain `:`
     */
    public readonly name: pulumi.Output<string>;

    /**
     * Create a LogStream resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LogStreamArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LogStreamArgs | LogStreamState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: LogStreamState = argsOrState as LogStreamState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["logGroupName"] = state ? state.logGroupName : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as LogStreamArgs | undefined;
            if (!args || args.logGroupName === undefined) {
                throw new Error("Missing required property 'logGroupName'");
            }
            inputs["logGroupName"] = args ? args.logGroupName : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:cloudwatch/logStream:LogStream", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LogStream resources.
 */
export interface LogStreamState {
    /**
     * The Amazon Resource Name (ARN) specifying the log stream.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The name of the log group under which the log stream is to be created.
     */
    readonly logGroupName?: pulumi.Input<string>;
    /**
     * The name of the log stream. Must not be longer than 512 characters and must not contain `:`
     */
    readonly name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a LogStream resource.
 */
export interface LogStreamArgs {
    /**
     * The name of the log group under which the log stream is to be created.
     */
    readonly logGroupName: pulumi.Input<string>;
    /**
     * The name of the log stream. Must not be longer than 512 characters and must not contain `:`
     */
    readonly name?: pulumi.Input<string>;
}
