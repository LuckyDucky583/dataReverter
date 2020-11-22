#!/usr/bin/env python3

import os
import logging
import boto3
import botocore

LOGGER = logging.getLogger()
LOGGER.setLevel(logging.INFO)

REGION = os.environ.get('REGION')

s3 = boto3.resource('s3', region_name=REGION)


def handler(event, context):
    LOGGER.info('Event structure: %s', event)

    for record in event['Records']:
        src_bucket = record['s3']['bucket']['name']
        src_key = record['s3']['object']['key']

        original = {
            'Bucket': src_bucket,
            'Key': src_key
        }

        text = s3.Object(src_bucket, src_key)
        data = text.get()['Body'].read().decode('utf-8')
        data_1 = data[::-1]
        LOGGER.info(data_1)

        LOGGER.info('copy_source: %s', data_1)
       # s3.upload_file(data_1, 'reversebucket58366', src_key + '-reversed')
        s3.Object('reversebucket58366', src_key + '-reversed').put(Body=data_1)

    return {
        'status': 'ok'
    }
