# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class EventSourceMapping(pulumi.CustomResource):
    """
    Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB and SQS
    
    For information about Lambda and how to use it, see [What is AWS Lambda?][1]
    For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.
    """
    def __init__(__self__, __name__, __opts__=None, batch_size=None, enabled=None, event_source_arn=None, function_name=None, starting_position=None, starting_position_timestamp=None):
        """Create a EventSourceMapping resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['batch_size'] = batch_size

        __props__['enabled'] = enabled

        if not event_source_arn:
            raise TypeError('Missing required property event_source_arn')
        __props__['event_source_arn'] = event_source_arn

        if not function_name:
            raise TypeError('Missing required property function_name')
        __props__['function_name'] = function_name

        __props__['starting_position'] = starting_position

        __props__['starting_position_timestamp'] = starting_position_timestamp

        __props__['function_arn'] = None
        __props__['last_modified'] = None
        __props__['last_processing_result'] = None
        __props__['state'] = None
        __props__['state_transition_reason'] = None
        __props__['uuid'] = None

        super(EventSourceMapping, __self__).__init__(
            'aws:lambda/eventSourceMapping:EventSourceMapping',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

