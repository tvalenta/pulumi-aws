# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class MainRouteTableAssociation(pulumi.CustomResource):
    original_route_table_id: pulumi.Output[str]
    """
    Used internally, see __Notes__ below
    """
    route_table_id: pulumi.Output[str]
    """
    The ID of the Route Table to set as the new
    main route table for the target VPC
    """
    vpc_id: pulumi.Output[str]
    """
    The ID of the VPC whose main route table should be set
    """
    def __init__(__self__, __name__, __opts__=None, route_table_id=None, vpc_id=None):
        """
        Provides a resource for managing the main routing table of a VPC.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] route_table_id: The ID of the Route Table to set as the new
               main route table for the target VPC
        :param pulumi.Input[str] vpc_id: The ID of the VPC whose main route table should be set
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not route_table_id:
            raise TypeError('Missing required property route_table_id')
        __props__['route_table_id'] = route_table_id

        if not vpc_id:
            raise TypeError('Missing required property vpc_id')
        __props__['vpc_id'] = vpc_id

        __props__['original_route_table_id'] = None

        super(MainRouteTableAssociation, __self__).__init__(
            'aws:ec2/mainRouteTableAssociation:MainRouteTableAssociation',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

