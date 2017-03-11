#!usr/bin/python
#Fri Mar 10 23:28:16 IST 2017
import boto3
import botocore
import os


#Usage:Set your IAM keys in the enviroment ~/.aws/credentials
#This script creates a VPC with a single public subnet


#variables
vpc_cidr = '10.0.0.0/16'
vpc_tenancy = 'default'
dry_run_true = True
dry_run_false= False
rt_cidr="0.0.0.0/0"
#########################
subnet_cidr = '10.0.1.0/24'

#create global client connection to the EC2
client = boto3.client('ec2')

print "------"*22
print"\t\t\t\t VPC with a single Public Subnet"
print "------"*22

print "Connected to EC2"

  #methods
def vpc_create():
    try:

        """ This function creates the VPC """
        print "Created VPC with id: "
        response_create_vpc = client.create_vpc(
            DryRun=dry_run_false,
            CidrBlock=vpc_cidr,
            InstanceTenancy=vpc_tenancy
            )

        vpc_id = response_create_vpc['Vpc']
        vpcid = vpc_id['VpcId']
        print vpcid

        #""" This function creates the Subnet"""
        response_create_subnet = client.create_subnet(
                DryRun=dry_run_false,
                CidrBlock =subnet_cidr,
                VpcId=vpcid
                )
        print "Created subnet  with id: "
        subnet_id=response_create_subnet['Subnet']
        subnetid = subnet_id['SubnetId']
        print subnetid

        #"""This function creates the internet gateway"""
        response_create_igw =client.create_internet_gateway(
                DryRun=dry_run_false
                )
        print "Created the Internet Gateway(IGW) with id: "
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

        #ceate a route table
        print "Created a new Route Table "
        response_create_rt = client.create_route_table(
                DryRun=dry_run_false,
                VpcId=vpcid
                )
        rt_id = response_create_rt['RouteTable']
        rtid=rt_id['RouteTableId']
        print "Route Table id:  ",rtid

        #associate the subnet to the route table
        response_assoc_rt = client.associate_route_table(
                DryRun=dry_run_false,
                SubnetId=subnetid,
                RouteTableId=rtid
                )
        print "Associated the subnet "+   subnetid + " to the RouteTable "+ rtid

        print "Creating Route to the Internet by attaching the IGW in the RouteTable " + rtid
        response_create_route = client.create_route(
                DestinationCidrBlock=rt_cidr,
                GatewayId=igwid,
                RouteTableId=rtid
                )
        print "Route created..... "+ subnetid +" is now a public subnet "
        #create a security group
        response_create_sg = client.create_security_group(
                DryRun=dry_run_false,
                GroupName=vpcid+"_security_group",
                Description=vpcid+"_security_group",
                VpcId=vpcid
                )
        print "Created the Secuirty Group"
        secgid =response_create_sg['GroupId']
        print "Secuirty Group Id",secgid

        #created the security groups"
        response_auth_secg_1=client.authorize_security_group_ingress(
                DryRun=dry_run_false,
                GroupId=secgid,
                IpProtocol='tcp',
                FromPort=22,
                ToPort=22,
                CidrIp='0.0.0.0/0'
               )

        response_auth_secg_2=client.authorize_security_group_ingress(
                DryRun=dry_run_false,
                GroupId=secgid,
                IpProtocol='tcp',
                FromPort=80,
                ToPort=80,
                CidrIp='0.0.0.0/0'
                )

        print "Ingress Rules for Secuirty Group "+secgid + " created Here is the response recieved\n"+str(response_auth_secg_1)
        print "Ingress Rules for Secuirty Group "+secgid + " created Here is the response recieved\n"+str(response_auth_secg_2)

        print "now creating a keypair to ssh into the instances"
        key_name =vpcid+"_key_pair.pem"

        response_create_key = client.create_key_pair(
                KeyName=vpcid+"Key_Pair"
                )
        crypto_key_data = response_create_key['KeyMaterial']

        print "Writing the key to "+ os.getcwd() + "/"+key_name
        key_file =open(key_name ,'w')
        key_file.write(crypto_key_data )
        key_file.close()

        print "Saved =>",key_name

        print "Securing the ",key_name
        os.system('chmod 400 *.pem')
        print "Permissions changed on the ",key_name


    except Exception as e:
        print "ERROR=>\n" ,e

#main method
def main():
    vpc_create()



if __name__ == "__main__":
    main()





