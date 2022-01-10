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
host = 'https://search-restaurants-rld4hzfcwan24qafiblj5ieoni.us-east-1.es.amazonaws.com'
index = 'restaurants'
url = host + '/' + index + '/_search'

dynamodb = boto3.resource('dynamodb')

es_client = Elasticsearch(
    hosts='https://search-news-db-newsrec-iumuowftmdt3zywn2i6x2ixf6q.us-west-2.es.amazonaws.com',
    http_auth=("roy123", "Ruoyu123#")
)

SENDER = "News Recommendation <yl4838@columbia.edu>"
RECIPIENT = "yl4838@columbia.edu"
CHARSET = "UTF-8"
SUBJECT = "Todays News Recommendation!"

client = boto3.client('ses')

def get_most_viewed_topic(views):
    topic = ""
    max_count = 0
    for k, v in views.items():
        if int(v) > max_count:
            max_count = int(v)
            topic = k
    return topic
    

def lambda_handler(event, context):
    user_table = dynamodb.Table('user_test')
    items = user_table.scan()['Items']
    today = datetime.now() - timedelta(days=1)
    today = today.replace(hour=0, minute=0, second=0, microsecond=0)
    t = Decimal(time.mktime(today.timetuple()))
    print("????, ", t)
    for user in items:
        if user["views"]:
            email = user["email"]
            topic = get_most_viewed_topic(user["views"])
            query = {
                "size": 3,
                "query": {
                    "query_string": {
                        "default_field": "category",
                        "query": topic
                    }
                }
            }
            searchParam = {
                "size": 1000,
                "query": {
                    "match": {
                        "labels": topic
                    }
                }
            }
            print("xxx", topic)
            res = es_client.search(index="news", body=searchParam)
            news_ids = []
            for hit in res["hits"]["hits"]:
                item = hit["_source"]
                news_id = item["id"]
                news_ids.append(news_id)
            
            print("yyy", news_ids)
            news = []
            news_table = dynamodb.Table('news-6998')
            for news_id in news_ids:
                response = news_table.query(KeyConditionExpression=Key('id').eq(news_id))
                print("!!! ", response)
                if "Items" in response:
                    item = response['Items']
                    if item[0]["insert_time"].compare(t) == 1:
                        news.append(item[0]["body"])
            
            news_to_send = min(len(news), 3)
            BODY_TEXT = "Hello! Here are my news recommendations for today for the topic {}.".format(topic)
            for i in range(news_to_send):
                BODY_TEXT +=  "\n\n{}: {}".format(i + 1, news[i])
            BODY_TEXT = (BODY_TEXT)
            # print(BODY_TEXT)
            try:
                # Provide the contents of the email.
                response = client.send_email(
                    Destination={
                        'ToAddresses': [
                            email,
                        ],
                    },
                    Message={
                        'Body': {
                            'Text': {
                                'Charset': CHARSET,
                                'Data': BODY_TEXT,
                            },
                        },
                        'Subject': {
                            'Charset': CHARSET,
                            'Data': SUBJECT,
                        },
                    },
                    Source=SENDER
                )
            # Display an error if something goes wrong. 
            except ClientError as e:
                print(e.response['Error']['Message'])
            else:
                print("Email sent! Message ID:"),
                print(response['MessageId'])