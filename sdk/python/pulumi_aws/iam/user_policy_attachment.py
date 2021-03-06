# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class UserPolicyAttachment(pulumi.CustomResource):
    policy_arn: pulumi.Output[str]
    """
    The ARN of the policy you want to apply
    """
    user: pulumi.Output[str]
    """
    The user the policy should be applied to
    """
    def __init__(__self__, __name__, __opts__=None, policy_arn=None, user=None):
        """
        Attaches a Managed IAM Policy to an IAM user
        
        > **NOTE:** The usage of this resource conflicts with the `aws_iam_policy_attachment` resource and will permanently show a difference if both are defined.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] policy_arn: The ARN of the policy you want to apply
        :param pulumi.Input[str] user: The user the policy should be applied to
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not policy_arn:
            raise TypeError('Missing required property policy_arn')
        __props__['policy_arn'] = policy_arn

        if not user:
            raise TypeError('Missing required property user')
        __props__['user'] = user

        super(UserPolicyAttachment, __self__).__init__(
            'aws:iam/userPolicyAttachment:UserPolicyAttachment',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

