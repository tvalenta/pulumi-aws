# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventPermission(pulumi.CustomResource):
    action: pulumi.Output[str]
    """
    The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.
    """
    condition: pulumi.Output[dict]
    """
    Configuration block to limit the event bus permissions you are granting to only accounts that fulfill the condition. Specified below.
    """
    principal: pulumi.Output[str]
    """
    The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus, optionally limited by `condition`.
    """
    statement_id: pulumi.Output[str]
    """
    An identifier string for the external account that you are granting permissions to.
    """
    def __init__(__self__, __name__, __opts__=None, action=None, condition=None, principal=None, statement_id=None):
        """
        Provides a resource to create a CloudWatch Events permission to support cross-account events in the current account default event bus.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] action: The action that you are enabling the other account to perform. Defaults to `events:PutEvents`.
        :param pulumi.Input[dict] condition: Configuration block to limit the event bus permissions you are granting to only accounts that fulfill the condition. Specified below.
        :param pulumi.Input[str] principal: The 12-digit AWS account ID that you are permitting to put events to your default event bus. Specify `*` to permit any account to put events to your default event bus, optionally limited by `condition`.
        :param pulumi.Input[str] statement_id: An identifier string for the external account that you are granting permissions to.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['action'] = action

        __props__['condition'] = condition

        if not principal:
            raise TypeError('Missing required property principal')
        __props__['principal'] = principal

        if not statement_id:
            raise TypeError('Missing required property statement_id')
        __props__['statement_id'] = statement_id

        super(EventPermission, __self__).__init__(
            'aws:cloudwatch/eventPermission:EventPermission',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

