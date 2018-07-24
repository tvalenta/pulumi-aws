// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";

import {Tags} from "../index";

/**
 * Provides an Neptune subnet group resource.
 */
export class SubnetGroup extends pulumi.CustomResource {
    /**
     * Get an existing SubnetGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SubnetGroupState): SubnetGroup {
        return new SubnetGroup(name, <any>state, { id });
    }

    /**
     * The ARN of the neptune subnet group.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The description of the neptune subnet group. Defaults to "Managed by Terraform".
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.
     */
    public readonly name: pulumi.Output<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    public readonly namePrefix: pulumi.Output<string>;
    /**
     * A list of VPC subnet IDs.
     */
    public readonly subnetIds: pulumi.Output<string[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    public readonly tags: pulumi.Output<Tags | undefined>;

    /**
     * Create a SubnetGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SubnetGroupArgs, opts?: pulumi.ResourceOptions)
    constructor(name: string, argsOrState?: SubnetGroupArgs | SubnetGroupState, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SubnetGroupState = argsOrState as SubnetGroupState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namePrefix"] = state ? state.namePrefix : undefined;
            inputs["subnetIds"] = state ? state.subnetIds : undefined;
            inputs["tags"] = state ? state.tags : undefined;
        } else {
            const args = argsOrState as SubnetGroupArgs | undefined;
            if (!args || args.subnetIds === undefined) {
                throw new Error("Missing required property 'subnetIds'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namePrefix"] = args ? args.namePrefix : undefined;
            inputs["subnetIds"] = args ? args.subnetIds : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:neptune/subnetGroup:SubnetGroup", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SubnetGroup resources.
 */
export interface SubnetGroupState {
    /**
     * The ARN of the neptune subnet group.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The description of the neptune subnet group. Defaults to "Managed by Terraform".
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    readonly namePrefix?: pulumi.Input<string>;
    /**
     * A list of VPC subnet IDs.
     */
    readonly subnetIds?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<Tags>;
}

/**
 * The set of arguments for constructing a SubnetGroup resource.
 */
export interface SubnetGroupArgs {
    /**
     * The description of the neptune subnet group. Defaults to "Managed by Terraform".
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the neptune subnet group. If omitted, Terraform will assign a random, unique name.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Creates a unique name beginning with the specified prefix. Conflicts with `name`.
     */
    readonly namePrefix?: pulumi.Input<string>;
    /**
     * A list of VPC subnet IDs.
     */
    readonly subnetIds: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A mapping of tags to assign to the resource.
     */
    readonly tags?: pulumi.Input<Tags>;
}