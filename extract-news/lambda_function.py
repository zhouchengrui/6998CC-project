import json
import requests
import time
import datetime
import aylien_news_api
from aylien_news_api.rest import ApiException
import boto3

dynamodb = boto3.resource('dynamodb')
configuration = aylien_news_api.Configuration()

# Configure API key authorization: app_id
configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = ''

# Configure API key authorization: app_key
configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = ''

# Defining host is optional and default to https://api.aylien.com/news
configuration.host = "https://api.aylien.com/news"
# Create an instance of the API class
api_instance = aylien_news_api.DefaultApi(aylien_news_api.ApiClient(configuration))

subscription_key = "1adef2341407443d9c916d929b20e00b"
search_url = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"

es_endpoint = "https://search-news-db-newsrec-iumuowftmdt3zywn2i6x2ixf6q.us-west-2.es.amazonaws.com/news/_bulk"

# keys in each records that should be removed
def load_items(data):
    table = dynamodb.Table('news-6998')
    for item in data:
        # convert float to Decimal
        table.put_item(Item=item)

def extract_trending_topics():
    subscription_key = "1adef2341407443d9c916d929b20e00b"
    search_url = "https://api.bing.microsoft.com/v7.0/news/trendingtopics"
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"textDecorations": True, "textFormat": "HTML", "count": 100}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = json.dumps(response.json())
    results = response.json()
    names = [article["name"] for article in results["value"]]
    
    return names

def extract_news_contents(names):
    # Configure API key authorization: app_id
    configuration.api_key['X-AYLIEN-NewsAPI-Application-ID'] = '84865697'

    # Configure API key authorization: app_key
    configuration.api_key['X-AYLIEN-NewsAPI-Application-Key'] = '84022274d19c8666b34a69c7630d1ff1'

    # Defining host is optional and default to https://api.aylien.com/news
    configuration.host = "https://api.aylien.com/news"
    # Create an instance of the API class
    api_instance = aylien_news_api.DefaultApi(aylien_news_api.ApiClient(configuration))
    
    url = "https://api.meaningcloud.com/deepcategorization-1.0"
    
    news = []

    x = datetime.datetime.now()
    try:
        # List Stories
        for topic in names:
            opts = {
                'title': topic,
                'published_at_start': 'NOW-1DAYS',
                'published_at_end': 'NOW',
                'language': ["en"],
                'sort_by': 'relevance',
                'per_page': 2
            }
            api_response = api_instance.list_stories(**opts)
            story = api_response.stories
            for s in story:
                new = {
                    "id": s.id,
                    "body": s.body,
                    "insert_time": str(x),
                }
                payload={
                    'key': '4ada1634e4a5eab15f176e6a4cae50c9',
                    'txt': s.body,
                    'model': 'IAB_2.0_en',  # like IAB_2.0_en
                }
                response = requests.post(url, data=payload).json()
                categories = s.keywords[:min(1, len(s.keywords))]
                for cat in response['category_list']:
                    categories.append(cat['label'].split(">")[0])
                new['labels'] = categories
                news.append(new)
                
        return news
    except ApiException as e:
        print("Exception when calling DefaultApi->list_stories: %s\n" % e)

def export_to_es(data):
    cnt = 0
    output = ""
    for n in data:
        for label in n['labels']:
            output += '{{ "index" : {{ "_index": "news", "_id" : "{}" }} }}\n'.format(cnt)
            output += '{{"id": "{}", "labels": "{}"}}\n'.format(n['id'], label)
            cnt += 1
    print(cnt)

    return json.dumps(output)

def lambda_handler(event, context):
    # TODO implement
    # names = extract_trending_topics()
    # news = extract_news_contents(names)
    # load_items(news)
    # data = export_to_es(news)
    # headers = {
    #     'Content-Type': 'application/json',
    # }
    # response = requests.post('https://search-news-db-newsrec-iumuowftmdt3zywn2i6x2ixf6q.us-west-2.es.amazonaws.com/news/_bulk', headers=headers, data=data, auth=('roy123', 'Ruoyu123#'))
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
