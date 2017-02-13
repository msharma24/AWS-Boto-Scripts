#!usr/bin/python
#Fri Feb 10 22:27:42 IST 2017
"""
Pass the S3 buket name as command line argument to check its availbility in your S3
"""
import argparse
import boto3

parser = argparse.ArgumentParser(description="Script To check if the bucket exists")
parser.add_argument('bucket',help="Enter the name of the S3 Bucket as a command line argument")
args = parser.parse_args()

def bucket_check(bucket_name):

        s3 = boto3.resource('s3')
        bucket = s3.Bucket(bucket_name)
        print "\n\n\t Looking up the bucket ==>> ",bucket_name
        if s3.Bucket(bucket_name) in s3.buckets.all():
            print "\n\n\tTrue! Bucket Exists ==>", bucket_name
        else:
            print "\n\n\t False! Bucket Does not Exists == >",bucket_name

if __name__ == "__main__":
    bucket_check(args.bucket)



