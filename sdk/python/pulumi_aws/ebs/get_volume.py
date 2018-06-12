# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime

class GetVolumeResult(object):
    """
    A collection of values returned by getVolume.
    """
    def __init__(__self__, arn=None, availability_zone=None, encrypted=None, iops=None, kms_key_id=None, size=None, snapshot_id=None, tags=None, volume_id=None, volume_type=None):
        if arn and not isinstance(arn, basestring):
            raise TypeError('Expected argument arn to be a basestring')
        __self__.arn = arn
        """
        The volume ARN (e.g. arn:aws:ec2:us-east-1:0123456789012:volume/vol-59fcb34e).
        """
        if availability_zone and not isinstance(availability_zone, basestring):
            raise TypeError('Expected argument availability_zone to be a basestring')
        __self__.availability_zone = availability_zone
        """
        The AZ where the EBS volume exists.
        """
        if encrypted and not isinstance(encrypted, bool):
            raise TypeError('Expected argument encrypted to be a bool')
        __self__.encrypted = encrypted
        """
        Whether the disk is encrypted.
        """
        if iops and not isinstance(iops, int):
            raise TypeError('Expected argument iops to be a int')
        __self__.iops = iops
        """
        The amount of IOPS for the disk.
        """
        if kms_key_id and not isinstance(kms_key_id, basestring):
            raise TypeError('Expected argument kms_key_id to be a basestring')
        __self__.kms_key_id = kms_key_id
        """
        The ARN for the KMS encryption key.
        """
        if size and not isinstance(size, int):
            raise TypeError('Expected argument size to be a int')
        __self__.size = size
        """
        The size of the drive in GiBs.
        """
        if snapshot_id and not isinstance(snapshot_id, basestring):
            raise TypeError('Expected argument snapshot_id to be a basestring')
        __self__.snapshot_id = snapshot_id
        """
        The snapshot_id the EBS volume is based off.
        """
        if tags and not isinstance(tags, dict):
            raise TypeError('Expected argument tags to be a dict')
        __self__.tags = tags
        """
        A mapping of tags for the resource.
        """
        if volume_id and not isinstance(volume_id, basestring):
            raise TypeError('Expected argument volume_id to be a basestring')
        __self__.volume_id = volume_id
        """
        The volume ID (e.g. vol-59fcb34e).
        """
        if volume_type and not isinstance(volume_type, basestring):
            raise TypeError('Expected argument volume_type to be a basestring')
        __self__.volume_type = volume_type
        """
        The type of EBS volume.
        """

def get_volume(filters=None, most_recent=None, tags=None):
    """
    Use this data source to get information about an EBS volume for use in other
    resources.
    """
    __args__ = dict()

    __args__['filters'] = filters
    __args__['mostRecent'] = most_recent
    __args__['tags'] = tags
    __ret__ = pulumi.runtime.invoke('aws:ebs/getVolume:getVolume', __args__)

    return GetVolumeResult(
        arn=__ret__.get('arn'),
        availability_zone=__ret__.get('availabilityZone'),
        encrypted=__ret__.get('encrypted'),
        iops=__ret__.get('iops'),
        kms_key_id=__ret__.get('kmsKeyId'),
        size=__ret__.get('size'),
        snapshot_id=__ret__.get('snapshotId'),
        tags=__ret__.get('tags'),
        volume_id=__ret__.get('volumeId'),
        volume_type=__ret__.get('volumeType'))