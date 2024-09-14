"""This module will have necessary functions to work 
with AWS EC2
"""

import boto3


def get_client(region="ap-south-1"):
    """This method gets the ec2 client with cli credentials"""
    return boto3.client("ec2", region_name=region)


def start_ec2(instance_id: str, region="ap-south-1") -> None:
    """This method starts an ec2 instance

    Args:
        instance_id (str): instance id
    """
    client = get_client(region)
    response = client.start_instances(InstanceIds=[instance_id])
    state = response["StartingInstances"][0]["CurrentState"]["Name"]
    print(f"instance with id {instance_id} is in {state} state")


def stop_ec2(instance_id: str, region="ap-south-1") -> None:
    """This method stops an ec2 instance

    Args:
        instance_id (str): instance id
    """
    client = get_client(region)
    response = client.stop_instances(InstanceIds=[instance_id])
    state = response["StoppingInstances"][0]["CurrentState"]["Name"]
    print(f"instance with id {instance_id} is in {state} state")


def get_valid_regions():
    """This method returns valid regions active for my account"""
    regions_response = get_client().describe_regions()
    for region_response in regions_response["Regions"]:
        yield region_response["RegionName"]


def get_all_ec2_by_tag(tagname: str, tagvalue: str, action: str):
    """This method gets all the ec2 instances and performs
    action (start, stop)
    """
    for region in get_valid_regions():
        # lets get all the ec2 instances by the tags
        # create an ec2 client of a specific region
        client = get_client(region)
        print(f"searching in {region} for ec2 instances")
        instances_response = client.describe_instances(
            Filters=[
                {
                    "Name": f"tag:{tagname}",
                    "Values": [
                        tagvalue,
                    ],
                },
            ]
        )
        if len(instances_response['Reservations']) == 0:
            print(f"no instances found in {region}")
            continue
        for instance_response in instances_response['Reservations'][0]['Instances']:
            instance_id = instance_response['InstanceId']
            print(f"found instance with id {instance_id}")
            if action == 'start':
                start_ec2(instance_id,region)
            elif action == 'stop':
                stop_ec2(instance_id,region)




if __name__ == "__main__":
    get_all_ec2_by_tag(tagname="Env", tagvalue="Dev", action="stop")
