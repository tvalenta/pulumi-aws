# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Template(pulumi.CustomResource):
    html: pulumi.Output[str]
    """
    The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
    """
    name: pulumi.Output[str]
    """
    The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
    """
    subject: pulumi.Output[str]
    """
    The subject line of the email.
    """
    text: pulumi.Output[str]
    """
    The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
    """
    def __init__(__self__, __name__, __opts__=None, html=None, name=None, subject=None, text=None):
        """
        Provides a resource to create a SES template.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] html: The HTML body of the email. Must be less than 500KB in size, including both the text and HTML parts.
        :param pulumi.Input[str] name: The name of the template. Cannot exceed 64 characters. You will refer to this name when you send email.
        :param pulumi.Input[str] subject: The subject line of the email.
        :param pulumi.Input[str] text: The email body that will be visible to recipients whose email clients do not display HTML. Must be less than 500KB in size, including both the text and HTML parts.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['html'] = html

        __props__['name'] = name

        __props__['subject'] = subject

        __props__['text'] = text

        super(Template, __self__).__init__(
            'aws:ses/template:Template',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

