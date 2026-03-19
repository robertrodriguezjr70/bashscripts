#!/usr/bin/env python3
import boto3
from datetime import datetime

def find_unused_volumes():
    ec2 = boto3.client('ec2')
    
    # Get all volumes
    response = ec2.describe_volumes()
    
    unused_volumes = []
    total_size = 0
    
    for volume in response['Volumes']:
        volume_id = volume['VolumeId']
        size = volume['Size']
        state = volume['State']
        
        # Check if volume is not attached to any instance
        if len(volume['Attachments']) == 0 and state == 'available':
            unused_volumes.append({
                'VolumeId': volume_id,
                'Size': size,
                'VolumeType': volume['VolumeType'],
                'CreateTime': volume['CreateTime'],
                'AvailabilityZone': volume['AvailabilityZone']
            })
            total_size += size
    
    # Print results
    if unused_volumes:
        print(f"\nFound {len(unused_volumes)} unused volumes:\n")
        print(f"{'Volume ID':<25} {'Size (GB)':<12} {'Type':<12} {'AZ':<15} {'Created'}")
        print("-" * 90)
        
        for vol in unused_volumes:
            created = vol['CreateTime'].strftime('%Y-%m-%d')
            print(f"{vol['VolumeId']:<25} {vol['Size']:<12} {vol['VolumeType']:<12} {vol['AvailabilityZone']:<15} {created}")
        
        print(f"\nTotal unused storage: {total_size} GB")
    else:
        print("\nNo unused volumes found.")

if __name__ == "__main__":
    try:
        find_unused_volumes()
    except Exception as e:
        print(f"Error: {str(e)}")
