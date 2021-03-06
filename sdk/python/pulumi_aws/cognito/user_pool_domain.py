# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class UserPoolDomain(pulumi.CustomResource):
    aws_account_id: pulumi.Output[str]
    """
    The AWS account ID for the user pool owner.
    """
    certificate_arn: pulumi.Output[str]
    """
    The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.
    """
    cloudfront_distribution_arn: pulumi.Output[str]
    """
    The ARN of the CloudFront distribution.
    """
    domain: pulumi.Output[str]
    """
    The domain string.
    """
    s3_bucket: pulumi.Output[str]
    """
    The S3 bucket where the static files for this domain are stored.
    """
    user_pool_id: pulumi.Output[str]
    """
    The user pool ID.
    """
    version: pulumi.Output[str]
    """
    The app version.
    """
    def __init__(__self__, __name__, __opts__=None, certificate_arn=None, domain=None, user_pool_id=None):
        """
        Provides a Cognito User Pool Domain resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] certificate_arn: The ARN of an ISSUED ACM certificate in us-east-1 for a custom domain.
        :param pulumi.Input[str] domain: The domain string.
        :param pulumi.Input[str] user_pool_id: The user pool ID.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['certificate_arn'] = certificate_arn

        if not domain:
            raise TypeError('Missing required property domain')
        __props__['domain'] = domain

        if not user_pool_id:
            raise TypeError('Missing required property user_pool_id')
        __props__['user_pool_id'] = user_pool_id

        __props__['aws_account_id'] = None
        __props__['cloudfront_distribution_arn'] = None
        __props__['s3_bucket'] = None
        __props__['version'] = None

        super(UserPoolDomain, __self__).__init__(
            'aws:cognito/userPoolDomain:UserPoolDomain',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

