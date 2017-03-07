#!usr/bin/python

#Mon Mar  6 22:20:52 IST 2017
#Mukesh Sharma
#Pass the vpcid to get detailed infromation about the vpc
#Prerequisites please have your IAM API Access Key and Secret Access Key set up in ~/.aws/credentials file

import boto3
import botocore
import argparse

def all_vpc_id():
    try:
        client = boto3.client('ec2')
        vpc_details = client.describe_vpcs()

        for vpc_id in vpc_details['Vpcs']:
            print "VPC ID List \n"
            print vpc_id['VpcId']

        print "run --vpcid VPCID as optional argument to get all the vpc information"
    except Exception as e:
        print "Error =>",e



def vpc_definition():
    try:
        #create the client session for ec2
        client = boto3.client('ec2')
        vpc_details = client.describe_vpcs(VpcIds=[args.vpcid])

        print "Displaying the VPC information :"

        for data in vpc_details['Vpcs']:
            print "VPC ID =>",data['VpcId']
            print "Tenancy =>",data['InstanceTenancy']
            print "State   =>",data['State']
            print "CIDR    =>",data['CidrBlock']
            tags = str(data['Tags'])
            tags_list = []
            tags_list = tags
            print "Vpc Tag Name =>",tags_list[13:-19]

    except Exception as e:
            print "ERROR => ",e



if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="This script will show all your VPC information")
    parser.add_argument("--vpcid",help="Enter the VpcID as the optional argument")

    args = parser.parse_args()

##### Execute the  methods

    if args.vpcid:
        vpc_definition()
    else:
        all_vpc_id()













