# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

def get_hosted_zone_id(region=None):
    """
    Use this data source to get the HostedZoneId of the AWS Elastic Load Balancing HostedZoneId
    in a given region for the purpose of using in an AWS Route53 Alias.
    """
    __args__ = dict()

    __args__['region'] = region
    __ret__ = pulumi.runtime.invoke('aws:elasticloadbalancing/getHostedZoneId:getHostedZoneId', __args__)
