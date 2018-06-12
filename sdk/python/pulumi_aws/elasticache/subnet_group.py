# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class SubnetGroup(pulumi.CustomResource):
    """
    Provides an ElastiCache Subnet Group resource.
    
    ~> **NOTE:** ElastiCache Subnet Groups are only for use when working with an
    ElastiCache cluster **inside** of a VPC. If you are on EC2 Classic, see the
    [ElastiCache Security Group resource](elasticache_security_group.html).
    """
    def __init__(__self__, __name__, __opts__=None, description=None, name=None, subnet_ids=None):
        """Create a SubnetGroup resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if description and not isinstance(description, basestring):
            raise TypeError('Expected property description to be a basestring')
        __self__.description = description
        """
        Description for the cache subnet group. Defaults to "Managed by Terraform".
        """
        __props__['description'] = description

        if name and not isinstance(name, basestring):
            raise TypeError('Expected property name to be a basestring')
        __self__.name = name
        """
        Name for the cache subnet group. Elasticache converts this name to lowercase.
        """
        __props__['name'] = name

        if not subnet_ids:
            raise TypeError('Missing required property subnet_ids')
        elif not isinstance(subnet_ids, list):
            raise TypeError('Expected property subnet_ids to be a list')
        __self__.subnet_ids = subnet_ids
        """
        List of VPC Subnet IDs for the cache subnet group
        """
        __props__['subnetIds'] = subnet_ids

        super(SubnetGroup, __self__).__init__(
            'aws:elasticache/subnetGroup:SubnetGroup',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'description' in outs:
            self.description = outs['description']
        if 'name' in outs:
            self.name = outs['name']
        if 'subnetIds' in outs:
            self.subnet_ids = outs['subnetIds']