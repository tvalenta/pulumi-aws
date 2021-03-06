# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class PatchGroup(pulumi.CustomResource):
    baseline_id: pulumi.Output[str]
    """
    The ID of the patch baseline to register the patch group with.
    """
    patch_group: pulumi.Output[str]
    """
    The name of the patch group that should be registered with the patch baseline.
    """
    def __init__(__self__, __name__, __opts__=None, baseline_id=None, patch_group=None):
        """
        Provides an SSM Patch Group resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] baseline_id: The ID of the patch baseline to register the patch group with.
        :param pulumi.Input[str] patch_group: The name of the patch group that should be registered with the patch baseline.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not baseline_id:
            raise TypeError('Missing required property baseline_id')
        __props__['baseline_id'] = baseline_id

        if not patch_group:
            raise TypeError('Missing required property patch_group')
        __props__['patch_group'] = patch_group

        super(PatchGroup, __self__).__init__(
            'aws:ssm/patchGroup:PatchGroup',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

