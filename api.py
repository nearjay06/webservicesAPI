from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, Separator
from pprint import pprint

import requests

style = style_from_dict({
    Token.Separator: '#E3AF3F',
    Token.QuestionMark: '#673ab7 bold',
    Token.Selected: '#800000',  # default
    Token.Pointer: '#673ab7 bold',
    Token.Instruction: '',  # default
    Token.Answer: '#453032 bold',
    Token.Question: '',
    })

questions = [
    {
        'type': 'list',
        'message': 'Select news source',
        'name': 'news sources',
        'choices': [
            Separator('= News ='),
            {
                'name': 'bbc-news'
            },
            {
                'name': 'cnn'
            },
            {
                'name': 'al-jazeera-english'
            },
            Separator('= News ='),
            {
                'name': 'financial-post'
            },
            {
                'name': 'the-economist'
            },
            Separator('= The usual ='),
            {
                'name': 'techcrunch'
            },
            {
                'name': 'bloomberg'
            },
            {
                'name': 'entertainment-weekly'
            },
        ],
        'validate': lambda answer: 'Choose at least one news source.'
        if len(answer) == 0 else True
    }
]


answers = prompt(questions, style=style)
pprint(answers)
source = answers["news sources"]


class NewsSources:
    # def __init__(self):
    #     pass

    def get_headlines(self):
        source = answers["news sources"]
        api_url = 'https://newsapi.org/v2/top-headlines?sources=' + \
            source+'&apiKey=479334790e5343abb9a3b43228f4b465&pageSize=10'

        
        # response = requests.get(api_url)

        # data = response.json()

        print("Api url", api_url)
        response = requests.get(api_url)
        data=response.json()           


        article_data = data['articles']
        if response.status_code == 200:
            print("Request Successful")
        else:
            print("Request Unsuccessful")

        for article in article_data:
            print("Title: ", article["title"])
            print("description: ", article["description"])
            print("url: ", article["url"])

        return response.status_code,article_data

    # def addnumbers(self, a, b):
    #     return a+b



news_sources = NewsSources()
print(news_sources.get_headlines())


