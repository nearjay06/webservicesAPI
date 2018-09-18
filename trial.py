import json
import requests


def get_headlines(news_sources):

    api_url = "https://newsapi.org/v2/top-headlines?source={}&apiKey=4001b871e2e84e83a85fc135fffceb96".format(news_sources)


    response = requests.get(api_url)

    if response.status_code == 200:
        # return json.loads(response.content.decode('utf-8'))
        print(response.content.decode('utf-8'))
    else:
        return print('Something is wrong')

    # name = prompt("What iis your name")

get_headlines("variable")