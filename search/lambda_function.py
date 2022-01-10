import json
import boto3
import random
import requests
from boto3.dynamodb.conditions import Key
from requests_aws4auth import AWS4Auth
from botocore.exceptions import ClientError
from datetime import datetime, timedelta
import time
from decimal import *
from elasticsearch import Elasticsearch, RequestsHttpConnection

region = "us-west-2"
service = 'es'
credentials = boto3.Session().get_credentials()
awsauth = AWS4Auth(credentials.access_key, credentials.secret_key, region, service, session_token=credentials.token)

aws_access_key_id = ''
aws_secret_access_key = ''

dynamodb = boto3.resource('dynamodb')

es_client = Elasticsearch(
    hosts='https://search-news-db-newsrec-iumuowftmdt3zywn2i6x2ixf6q.us-west-2.es.amazonaws.com',
    http_auth=("roy123", "Ruoyu123#")
)


def lambda_handler(event, context):
    print(event)
    topic = event["queryStringParameters"]["q"]
    
    today = datetime.now() - timedelta(days=1)
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    t = Decimal(time.mktime(today.timetuple()))

    searchParam = {
        "size": 50,
        "query": {
            "match": {
                "labels": topic
            }
        }
    }
    res = es_client.search(index="news", body=searchParam)
    news_ids = []
    for hit in res["hits"]["hits"]:
        item = hit["_source"]
        news_id = item["id"]
        news_ids.append(news_id)
    print(news_ids)
    news = []
    news_table = dynamodb.Table('news-6998')
    for news_id in news_ids:
        response = news_table.query(KeyConditionExpression=Key('id').eq(news_id))
        if "Items" in response:
            item = response['Items']
            # if item[0]["insert_time"].compare(t) == 1:
            news.append([item[0]["body"], item[0]["id"]])
                
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
    
    
