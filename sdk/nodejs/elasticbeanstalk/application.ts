// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provides an Elastic Beanstalk Application Resource. Elastic Beanstalk allows
 * you to deploy and manage applications in the AWS cloud without worrying about
 * the infrastructure that runs those applications.
 * 
 * This resource creates an application that has one configuration template named
 * `default`, and no application versions
 */
export class Application extends pulumi.CustomResource {
    /**
     * Get an existing Application resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ApplicationState, opts?: pulumi.CustomResourceOptions): Application {
        return new Application(name, <any>state, { ...opts, id: id });
    }

    public readonly appversionLifecycle: pulumi.Output<{ deleteSourceFromS3?: boolean, maxAgeInDays?: number, maxCount?: number, serviceRole: string } | undefined>;
    /**
     * Short description of the application
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The name of the application, must be unique within your account
     */
    public readonly name: pulumi.Output<string>;

    /**
     * Create a Application resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ApplicationArgs | ApplicationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ApplicationState = argsOrState as ApplicationState | undefined;
            inputs["appversionLifecycle"] = state ? state.appversionLifecycle : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
        } else {
            const args = argsOrState as ApplicationArgs | undefined;
            inputs["appversionLifecycle"] = args ? args.appversionLifecycle : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
        }
        super("aws:elasticbeanstalk/application:Application", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Application resources.
 */
export interface ApplicationState {
    readonly appversionLifecycle?: pulumi.Input<{ deleteSourceFromS3?: pulumi.Input<boolean>, maxAgeInDays?: pulumi.Input<number>, maxCount?: pulumi.Input<number>, serviceRole: pulumi.Input<string> }>;
    /**
     * Short description of the application
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the application, must be unique within your account
     */
    readonly name?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Application resource.
 */
export interface ApplicationArgs {
    readonly appversionLifecycle?: pulumi.Input<{ deleteSourceFromS3?: pulumi.Input<boolean>, maxAgeInDays?: pulumi.Input<number>, maxCount?: pulumi.Input<number>, serviceRole: pulumi.Input<string> }>;
    /**
     * Short description of the application
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The name of the application, must be unique within your account
     */
    readonly name?: pulumi.Input<string>;
}
