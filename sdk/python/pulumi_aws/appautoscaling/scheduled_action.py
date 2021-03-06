# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ScheduledAction(pulumi.CustomResource):
    arn: pulumi.Output[str]
    """
    The Amazon Resource Name (ARN) of the scheduled action.
    """
    end_time: pulumi.Output[str]
    """
    The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z
    """
    name: pulumi.Output[str]
    """
    The name of the scheduled action.
    """
    resource_id: pulumi.Output[str]
    """
    The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)
    """
    scalable_dimension: pulumi.Output[str]
    """
    The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount
    """
    scalable_target_action: pulumi.Output[dict]
    """
    The new minimum and maximum capacity. You can set both values or just one. See below
    """
    schedule: pulumi.Output[str]
    """
    The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)
    """
    service_namespace: pulumi.Output[str]
    """
    The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs
    """
    start_time: pulumi.Output[str]
    """
    The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z
    """
    def __init__(__self__, __name__, __opts__=None, end_time=None, name=None, resource_id=None, scalable_dimension=None, scalable_target_action=None, schedule=None, service_namespace=None, start_time=None):
        """
        Provides an Application AutoScaling ScheduledAction resource.
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[str] end_time: The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z
        :param pulumi.Input[str] name: The name of the scheduled action.
        :param pulumi.Input[str] resource_id: The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId)
        :param pulumi.Input[str] scalable_dimension: The scalable dimension. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension) Example: ecs:service:DesiredCount
        :param pulumi.Input[dict] scalable_target_action: The new minimum and maximum capacity. You can set both values or just one. See below
        :param pulumi.Input[str] schedule: The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule)
        :param pulumi.Input[str] service_namespace: The namespace of the AWS service. Documentation can be found in the parameter at: [AWS Application Auto Scaling API Reference](https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace) Example: ecs
        :param pulumi.Input[str] start_time: The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z
        """
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['end_time'] = end_time

        __props__['name'] = name

        if not resource_id:
            raise TypeError('Missing required property resource_id')
        __props__['resource_id'] = resource_id

        __props__['scalable_dimension'] = scalable_dimension

        __props__['scalable_target_action'] = scalable_target_action

        __props__['schedule'] = schedule

        if not service_namespace:
            raise TypeError('Missing required property service_namespace')
        __props__['service_namespace'] = service_namespace

        __props__['start_time'] = start_time

        __props__['arn'] = None

        super(ScheduledAction, __self__).__init__(
            'aws:appautoscaling/scheduledAction:ScheduledAction',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

