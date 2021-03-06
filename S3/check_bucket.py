#!usr/bin/python
#Fri Feb 10 22:27:42 IST 2017

import argparse
import boto3

parser = argparse.ArgumentParser(description="Script To check if the bucket exists")
parser.add_argument('bucket',help="Enter the name of the S3 Bucket as a command line argument")
args = parser.parse_args()

def bucket_check(bucket_name):
    try:

        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        print "\n\n\t Looking up the bucket ==>> ",bucket_name
        if s3.Bucket(bucket_name) in s3.buckets.all():
            print "\n\n\t True! Bucket Exists ==>", bucket_name
        else:
            print "\n\n\t False! Bucket Does not Exists == >",bucket_name
    except Exception as e:
        print "Error =>",e

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script To check if the bucket exists")
    parser.add_argument('bucket',help="Enter the name of the S3 Bucket as a command line argument")
    args = parser.parse_args()

    bucket_check(args.bucket)



