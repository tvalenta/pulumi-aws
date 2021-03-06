# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Route(pulumi.CustomResource):
    destination_cidr_block: pulumi.Output[str]
    """
    IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
    """
    transit_gateway_attachment_id: pulumi.Output[str]
    """
    Identifier of EC2 Transit Gateway Attachment.
    """
    transit_gateway_route_table_id: pulumi.Output[str]
    """
    Identifier of EC2 Transit Gateway Route Table.
    """
    def __init__(__self__, __name__, __opts__=None, destination_cidr_block=None, transit_gateway_attachment_id=None, transit_gateway_route_table_id=None):
        """
        Manages an EC2 Transit Gateway Route.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] destination_cidr_block: IPv4 CIDR range used for destination matches. Routing decisions are based on the most specific match.
        :param pulumi.Input[str] transit_gateway_attachment_id: Identifier of EC2 Transit Gateway Attachment.
        :param pulumi.Input[str] transit_gateway_route_table_id: Identifier of EC2 Transit Gateway Route Table.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not destination_cidr_block:
            raise TypeError('Missing required property destination_cidr_block')
        __props__['destination_cidr_block'] = destination_cidr_block

        if not transit_gateway_attachment_id:
            raise TypeError('Missing required property transit_gateway_attachment_id')
        __props__['transit_gateway_attachment_id'] = transit_gateway_attachment_id

        if not transit_gateway_route_table_id:
            raise TypeError('Missing required property transit_gateway_route_table_id')
        __props__['transit_gateway_route_table_id'] = transit_gateway_route_table_id

        super(Route, __self__).__init__(
            'aws:ec2transitgateway/route:Route',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

