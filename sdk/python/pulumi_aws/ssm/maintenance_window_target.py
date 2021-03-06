# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class MaintenanceWindowTarget(pulumi.CustomResource):
    owner_information: pulumi.Output[str]
    """
    User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
    """
    resource_type: pulumi.Output[str]
    """
    The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
    """
    targets: pulumi.Output[list]
    """
    The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
    """
    window_id: pulumi.Output[str]
    """
    The Id of the maintenance window to register the target with.
    """
    def __init__(__self__, __name__, __opts__=None, owner_information=None, resource_type=None, targets=None, window_id=None):
        """
        Provides an SSM Maintenance Window Target resource
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] owner_information: User-provided value that will be included in any CloudWatch events raised while running tasks for these targets in this Maintenance Window.
        :param pulumi.Input[str] resource_type: The type of target being registered with the Maintenance Window. Possible values `INSTANCE`.
        :param pulumi.Input[list] targets: The targets (either instances or tags). Instances are specified using Key=instanceids,Values=instanceid1,instanceid2. Tags are specified using Key=tag name,Values=tag value.
        :param pulumi.Input[str] window_id: The Id of the maintenance window to register the target with.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['owner_information'] = owner_information

        if not resource_type:
            raise TypeError('Missing required property resource_type')
        __props__['resource_type'] = resource_type

        if not targets:
            raise TypeError('Missing required property targets')
        __props__['targets'] = targets

        if not window_id:
            raise TypeError('Missing required property window_id')
        __props__['window_id'] = window_id

        super(MaintenanceWindowTarget, __self__).__init__(
            'aws:ssm/maintenanceWindowTarget:MaintenanceWindowTarget',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

