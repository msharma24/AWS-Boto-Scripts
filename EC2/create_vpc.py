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

        """ This function creates the VPC """
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

        """ This function creates the Subnet"""
        response_create_subnet = client.create_subnet(
                DryRun=dry_run_false,
                CidrBlock =subnet_cidr,
                VpcId=vpcid
                )
        print "Created subnet "
        subnet_id=response_create_subnet['Subnet']
        subnetid = subnet_id['SubnetId']
        print subnetid

        """THis function creates the internet gateway"""
        response_create_igw =client.create_internet_gateway(
                DryRun=dry_run_false
                )
        print "Created the Internet Gateway"
        igw_id=response_create_igw['InternetGateway']
        igwid = igw_id['InternetGatewayId']
        print igwid

        #attach the internetgateway to the vpc
        response_atttach_igw = client.attach_internet_gateway(
                DryRun=dry_run_false,
                InternetGatewayId=igwid,
                VpcId=vpcid
                )
        print "Attached IGW " + igwid + " to the VPC " + vpcid






    except Exception as e:
        print "ERROR=>\n" ,e

#main method
def main():
    vpc_create()



if __name__ == "__main__":
    main()





