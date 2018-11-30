#!/usr/bin/python3

import boto3

import requests
response = requests.get('http://169.254.169.254/latest/meta-data/instance-id')
instance_id = response.text
response = requests.get('http://169.254.169.254/latest/meta-data/placement/availability-zone')
availability_zone = response.text

client = boto3.client('ec2', region_name='us-west-1')

for i in range(2):
    print('volume #' + str(i))
    response = client.create_volume(Size=1, VolumeType='gp2', AvailabilityZone=availability_zone,
            TagSpecifications=[{
                'ResourceType':'volume',
                'Tags': [
                    { 'Key': 'RAID', 'Value': 'YES' },
                    { 'Key': 'RAID_N', 'Value': str(i)}
                ]
            }])
    print(response['VolumeId'])
