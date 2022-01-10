import json
import boto3
import random
from boto3.dynamodb.conditions import Key
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')

def lambda_handler(event, context):
    print(event["queryStringParameters"])
    news_id = event["queryStringParameters"]["q"]
    username = event["queryStringParameters"]["username"]
    news_table = dynamodb.Table('news-6998')
    user_table = dynamodb.Table('user_test')
    response = news_table.query(KeyConditionExpression=Key('id').eq(news_id))
    news = []
    
    print(response)
    if "Items" in response:
        item = response['Items']
        news.append(item[0]["body"])
        labels = item[0]["labels"]
        for label in labels:
            views = user_table.get_item(Key={"user_id": username})["Item"]["views"]
            print(views)
            current_count = int(views[label]) if label in views else 0
            views[label] = current_count + 1
            
            user_table.update_item(
                Key={
                    'user_id': username,
                },
                UpdateExpression="set #views=:v",
                ExpressionAttributeValues={
                    ':v': views,
                },
                ExpressionAttributeNames={
                    "#views": "views"
                },
                ReturnValues="UPDATED_NEW"
            )
    
        
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
        'body': json.dumps(results)
    }
