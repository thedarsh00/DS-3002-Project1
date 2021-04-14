import pandas as pd
import boto3
import os
import sys

#read in AWS keys from environment variables
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

#reading in a file from Docker container as CSV
df = pd.read_csv("housing.csv")

#shape: rows, columns
print("Shape of the database, in the form (rows, columns)")
print(df.shape)

#removing two columns
print("Dropping two columns...")
df.drop("ocean_proximity", axis=1, inplace=True)
df.drop("households", axis=1, inplace=True)

#new shape: rows, columns
print("New shape")
print(df.shape)

#information about the dataset
print("Useful information about the dataset:")
print(df.info())

#converting to JSON
df.to_json('housing.json')

#send to s3
#establish boto3 session
session = boto3.Session(aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
s3 = boto3.resource('s3')

#create bucket
bucket_name = 'dp2bkq-project'
s3.create_bucket(Bucket=bucket_name)

#upload to bucket
print('Uploading to Amazon S3 bucket...')
s3.meta.client.upload_file('housing.json', 'dp2bkq-project-test', 'housing.json')

print("Succesfully uploaded!")