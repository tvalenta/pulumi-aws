# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class JobQueue(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name of the job queue.
    """
    compute_environments: pulumi.Output[list]
    """
    Specifies the set of compute environments
    mapped to a job queue and their order.  The position of the compute environments
    in the list will dictate the order. You can associate up to 3 compute environments
    with a job queue.
    """
    name: pulumi.Output[str]
    """
    Specifies the name of the job queue.
    """
    priority: pulumi.Output[int]
    """
    The priority of the job queue. Job queues with a higher priority
    are evaluated first when associated with the same compute environment.
    """
    state: pulumi.Output[str]
    """
    The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
    """
    def __init__(__self__, __name__, __opts__=None, compute_environments=None, name=None, priority=None, state=None):
        """
        Provides a Batch Job Queue resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[list] compute_environments: Specifies the set of compute environments
               mapped to a job queue and their order.  The position of the compute environments
               in the list will dictate the order. You can associate up to 3 compute environments
               with a job queue.
        :param pulumi.Input[str] name: Specifies the name of the job queue.
        :param pulumi.Input[int] priority: The priority of the job queue. Job queues with a higher priority
               are evaluated first when associated with the same compute environment.
        :param pulumi.Input[str] state: The state of the job queue. Must be one of: `ENABLED` or `DISABLED`
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not compute_environments:
            raise TypeError('Missing required property compute_environments')
        __props__['compute_environments'] = compute_environments

        __props__['name'] = name

        if not priority:
            raise TypeError('Missing required property priority')
        __props__['priority'] = priority

        if not state:
            raise TypeError('Missing required property state')
        __props__['state'] = state

        __props__['arn'] = None

        super(JobQueue, __self__).__init__(
            'aws:batch/jobQueue:JobQueue',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

