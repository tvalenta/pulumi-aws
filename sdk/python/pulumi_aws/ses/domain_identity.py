# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class DomainIdentity(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the domain identity.
    """
    domain: pulumi.Output[str]
    """
    The domain name to assign to SES
    """
    verification_token: pulumi.Output[str]
    """
    A code which when added to the domain as a TXT record
    will signal to SES that the owner of the domain has authorised SES to act on
    their behalf. The domain identity will be in state "verification pending"
    until this is done. See below for an example of how this might be achieved
    when the domain is hosted in Route 53 and managed by Terraform.  Find out
    more about verifying domains in Amazon SES in the [AWS SES
    docs](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-domains.html).
    """
    def __init__(__self__, __name__, __opts__=None, domain=None):
        """
        Provides an SES domain identity resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] domain: The domain name to assign to SES
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not domain:
            raise TypeError('Missing required property domain')
        __props__['domain'] = domain

        __props__['arn'] = None
        __props__['verification_token'] = None

        super(DomainIdentity, __self__).__init__(
            'aws:ses/domainIdentity:DomainIdentity',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

