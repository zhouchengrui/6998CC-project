import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
from datetime import datetime, timedelta
import time
from decimal import *

region = "use-west-2"
dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    # TODO implement
    print("event", event)
    today = datetime.now() - timedelta(days=1)
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    t = Decimal(time.mktime(today.timetuple()))
    print(t)
    
    table = dynamodb.Table('news-6998')
    response = table.scan(FilterExpression=Attr('insert_time').gte(t))
    # response = table.scan()
    data = response['Items']
    
    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])
    news = []
    i = 0
    for item in data:
        i += 1
        if i > 50:
            break
        news.append([item["body"], item["id"]])
    
    results = {
        'news': news
    }
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET',
        },
        'body': json.dumps(results),
        'isBase64Encoded': False
    }
