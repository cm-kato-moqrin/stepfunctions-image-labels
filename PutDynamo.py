import boto3
import json
from datetime import datetime

dynamodb_resource = boto3.resource('dynamodb')
table = dynamodb_resource.Table('ImageInfo')


def lambda_handler(event, context):

    id = event[0]['id']
    size = event[0]['size']
    IP = event[0]['IP']
    time = event[0]['time']
    file_name = event[0]['file_name']
    image_labeling = event[1]['labeling']

    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")

    # テーブル挿入
    table_put_item_response = table.put_item(
        Item={
            'id': id,
            'size': size,
            'IP': IP,
            'time': time,
            'file_name': file_name,
            'create_time_stamp': time_stamp,
            'detection': image_labeling
        }
    )
    return table_put_item_response
