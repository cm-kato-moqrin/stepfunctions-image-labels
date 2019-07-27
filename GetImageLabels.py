import boto3
import copy

rekognition_client = boto3.client('rekognition')
translate_client = boto3.client(service_name='translate', use_ssl=True)


def lambda_handler(event, context):

    id = event['id']
    fileName = event['detail']['requestParameters']['key']
    bucket = event['detail']['requestParameters']['bucketName']

    # 画像のラベル検出
    response = rekognition_client.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': fileName}})

    detect_dict = {}
    detect_dict['id'] = id
    detect_dict['labeling'] = {}

    temp_d = {}
    for i, label in enumerate(response['Labels']):
        # ラベルを日本語に翻訳
        labelName = translate_client.translate_text(Text=label['Name'],
                                                    SourceLanguageCode="en", TargetLanguageCode="ja").get('TranslatedText')
        temp_d['Label'] = labelName
        temp_d['Confidence'] = str(label['Confidence'])
        detect_dict['labeling'][i] = str(copy.deepcopy(temp_d))

    return detect_dict
