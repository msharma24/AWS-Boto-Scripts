#!usr/bin/python
#Fri Feb 10 10:56:20 IST 2017
#Mukesh Sharma
import boto3

"""
    Script to list all the S3 buckets
"""
s3 = boto3.resource('s3')
print "S3 Bucket List : "
for bucket in s3.buckets.all():
    print bucket.name
