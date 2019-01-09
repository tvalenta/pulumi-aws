// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Subscribes to a Security Hub product.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * 
 * const aws_securityhub_account_example = new aws.securityhub.Account("example", {});
 * const aws_region_current = pulumi.output(aws.getRegion({}));
 * const aws_securityhub_product_subscription_example = new aws.securityhub.ProductSubscription("example", {
 *     productArn: aws_region_current.apply(__arg0 => `arn:aws:securityhub:${__arg0.name}:733251395267:product/alertlogic/althreatmanagement`),
 * }, {dependsOn: [aws_securityhub_account_example]});
 * ```
 */
export class ProductSubscription extends pulumi.CustomResource {
    /**
     * Get an existing ProductSubscription resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProductSubscriptionState, opts?: pulumi.CustomResourceOptions): ProductSubscription {
        return new ProductSubscription(name, <any>state, { ...opts, id: id });
    }

    /**
     * The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
     */
    public /*out*/ readonly arn: pulumi.Output<string>;
    /**
     * The ARN of the product that generates findings that you want to import into Security Hub - see below.
     */
    public readonly productArn: pulumi.Output<string>;

    /**
     * Create a ProductSubscription resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ProductSubscriptionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ProductSubscriptionArgs | ProductSubscriptionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: ProductSubscriptionState = argsOrState as ProductSubscriptionState | undefined;
            inputs["arn"] = state ? state.arn : undefined;
            inputs["productArn"] = state ? state.productArn : undefined;
        } else {
            const args = argsOrState as ProductSubscriptionArgs | undefined;
            if (!args || args.productArn === undefined) {
                throw new Error("Missing required property 'productArn'");
            }
            inputs["productArn"] = args ? args.productArn : undefined;
            inputs["arn"] = undefined /*out*/;
        }
        super("aws:securityhub/productSubscription:ProductSubscription", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ProductSubscription resources.
 */
export interface ProductSubscriptionState {
    /**
     * The ARN of a resource that represents your subscription to the product that generates the findings that you want to import into Security Hub.
     */
    readonly arn?: pulumi.Input<string>;
    /**
     * The ARN of the product that generates findings that you want to import into Security Hub - see below.
     */
    readonly productArn?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ProductSubscription resource.
 */
export interface ProductSubscriptionArgs {
    /**
     * The ARN of the product that generates findings that you want to import into Security Hub - see below.
     */
    readonly productArn: pulumi.Input<string>;
}
