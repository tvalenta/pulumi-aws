// *** WARNING: this file was generated by the Pulumi Terraform Bridge (TFGEN) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as fabric from "@pulumi/pulumi-fabric";

/**
 * Registers an on-premises server or virtual machine with Amazon EC2 so that it can be managed using Run Command.
 */
export class Activation extends fabric.Resource {
    /**
     * The code the system generates when it processes the activation.
     */
    public /*out*/ readonly activationCode: fabric.Computed<string>;
    /**
     * The description of the resource that you want to register.
     */
    public readonly description?: fabric.Computed<string>;
    /**
     * The date by which this activation request should expire. The default value is 24 hours.
     */
    public readonly expirationDate?: fabric.Computed<string>;
    /**
     * If the current activation has expired.
     */
    public /*out*/ readonly expired: fabric.Computed<string>;
    /**
     * The IAM Role to attach to the managed instance.
     */
    public readonly iamRole: fabric.Computed<string>;
    /**
     * The default name of the registerd managed instance.
     */
    public readonly name: fabric.Computed<string>;
    /**
     * The number of managed instances that are currently registered using this activation.
     */
    public /*out*/ readonly registrationCount: fabric.Computed<number>;
    /**
     * The maximum number of managed instances you want to register. The default value is 1 instance.
     */
    public readonly registrationLimit?: fabric.Computed<number>;

    /**
     * Create a Activation resource with the given unique name, arguments and optional additional
     * resource dependencies.
     *
     * @param urnName A _unique_ name for this Activation instance
     * @param args A collection of arguments for creating this Activation intance
     * @param dependsOn A optional array of additional resources this intance depends on
     */
    constructor(urnName: string, args: ActivationArgs, dependsOn?: fabric.Resource[]) {
        if (args.iamRole === undefined) {
            throw new Error("Missing required property 'iamRole'");
        }
        super("aws:ssm/activation:Activation", urnName, {
            "description": args.description,
            "expirationDate": args.expirationDate,
            "iamRole": args.iamRole,
            "name": args.name,
            "registrationLimit": args.registrationLimit,
            "activationCode": undefined,
            "expired": undefined,
            "registrationCount": undefined,
        }, dependsOn);
    }
}

/**
 * The set of arguments for constructing a Activation resource.
 */
export interface ActivationArgs {
    /**
     * The description of the resource that you want to register.
     */
    readonly description?: fabric.ComputedValue<string>;
    /**
     * The date by which this activation request should expire. The default value is 24 hours.
     */
    readonly expirationDate?: fabric.ComputedValue<string>;
    /**
     * The IAM Role to attach to the managed instance.
     */
    readonly iamRole: fabric.ComputedValue<string>;
    /**
     * The default name of the registerd managed instance.
     */
    readonly name?: fabric.ComputedValue<string>;
    /**
     * The maximum number of managed instances you want to register. The default value is 1 instance.
     */
    readonly registrationLimit?: fabric.ComputedValue<number>;
}

