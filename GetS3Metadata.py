from datetime import datetime


def lambda_handler(event, context):
    id = event['id']
    time = event['time']
    size = event['detail']['additionalEventData']['bytesTransferredIn']
    IP = event['detail']['sourceIPAddress']
    fileName = event['detail']['requestParameters']['key']

    # 日時取得
    time_stamp = datetime.now().strftime("%Y%m%d%H%M%S")

    s3_meta_data = {}
    s3_meta_data['id'] = id
    s3_meta_data['size'] = str(size)
    s3_meta_data['time'] = time
    s3_meta_data['IP'] = IP
    s3_meta_data['fileName'] = fileName
    s3_meta_data['create_time_stamp'] = time_stamp

    return s3_meta_data
