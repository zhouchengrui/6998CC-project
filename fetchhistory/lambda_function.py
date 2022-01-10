import json
import boto3 
from boto3.dynamodb.conditions import Key, Attr
import requests
import idna
import requests_aws4auth
import chardet
import urllib3
import certifi


        
def lambda_handler(event, context):
    #username = event['queryStringParameters']['q']
    #print("----------usernmae is----------", username)
    username = "zxc"
    history = getUserHistory(username)
    return{
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Headers': 'Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With,x-api-key',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS, POST, GET',
        },
        'body': json.dumps(history)
    }

def getUserHistory(username):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table("user_test") 
    his = table.scan(FilterExpression=Attr('username').eq(username))
    #print(his)
    views = his["Items"][0]["views"]
    print(views)
    print(type(views))
    for a in views:
        views[a] = int(views[a])
        print(views[a])
    return views