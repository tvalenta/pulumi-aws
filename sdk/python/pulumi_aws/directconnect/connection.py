# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Connection(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The ARN of the connection.
    """
    bandwidth: pulumi.Output[str]
    """
    The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
    """
    jumbo_frame_capable: pulumi.Output[bool]
    """
    Boolean value representing if jumbo frames have been enabled for this connection.
    """
    location: pulumi.Output[str]
    """
    The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
    """
    name: pulumi.Output[str]
    """
    The name of the connection.
    """
    tags: pulumi.Output[dict]
    """
    A mapping of tags to assign to the resource.
    """
    def __init__(__self__, __name__, __opts__=None, bandwidth=None, location=None, name=None, tags=None):
        """
        Provides a Connection of Direct Connect.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] bandwidth: The bandwidth of the connection. Available values: 1Gbps, 10Gbps. Case sensitive.
        :param pulumi.Input[str] location: The AWS Direct Connect location where the connection is located. See [DescribeLocations](https://docs.aws.amazon.com/directconnect/latest/APIReference/API_DescribeLocations.html) for the list of AWS Direct Connect locations. Use `locationCode`.
        :param pulumi.Input[str] name: The name of the connection.
        :param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not bandwidth:
            raise TypeError('Missing required property bandwidth')
        __props__['bandwidth'] = bandwidth

        if not location:
            raise TypeError('Missing required property location')
        __props__['location'] = location

        __props__['name'] = name

        __props__['tags'] = tags

        __props__['arn'] = None
        __props__['jumbo_frame_capable'] = None

        super(Connection, __self__).__init__(
            'aws:directconnect/connection:Connection',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

