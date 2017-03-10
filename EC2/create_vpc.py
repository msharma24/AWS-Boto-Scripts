#!usr/bin/python
import boto3
import botocore
import logging

#variables
vpc_cidr = '10.0.0.0/16'
vpc_tenancy = 'default'
dry_run_true = True
dry_run_false= False
#########################
subnet_cidr = '10.0.1.0/24'

#create global the client connection to the EC2
client = boto3.client('ec2')
print "Connected to EC2"

#methods
def vpc_create():
    try:

        print "Creating VPC"
        response_create_vpc = client.create_vpc(
            DryRun=dry_run_false,
            CidrBlock=vpc_cidr,
            InstanceTenancy=vpc_tenancy
            )

        vpc_id = response_create_vpc['Vpc']
        #print vpc_id
        vpcid = vpc_id['VpcId']
        print vpcid
        #print vpc_id['VpcId']

        response_create_subnet = client.create_subnet(
                DryRun=dry_run_false,
                CidrBlock =subnet_cidr,
                VpcId=vpcid
                )
        print "Created subnet ",response_create_subnet

    except Exception as e:
        print "ERROR=>\n" ,e

#main method
def main():
    vpc_create()



if __name__ == "__main__":
    main()





