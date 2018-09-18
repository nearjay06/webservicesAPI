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
                'name': 'CNN'
            },
            {
                'name': 'ALJAZEERA'
            },
            Separator('= News ='),
            {
                'name': 'CNN',
                'checked': True
            },
            {
                'name': 'Euronews'
            },
            {
                'name': 'Sky News'
            },
            Separator('= The usual ='),
            {
                'name': 'Reuters'
            },
            {
                'name': 'Bloomberg'
            },
            {
                'name': 'NTV'
            },
            Separator('=The extras='),
            {
                'name': 'MSNBC'
            },
            {'name': 'Fox News',
                'disabled': 'out of service'
            },
            {'name': 'Washington Post'

                },
        ],
        'validate': lambda answer: 'You must choose at least one news source.'
        if len(answer) == 0 else True
    }
]


answers = prompt(questions, style=style)
# pprint(answers)
source=answers["news sources"]

def get_headlines():
    
    api_url = 'https://newsapi.org/v2/top-headlines?sources='+source+'&pageSize=10&apiKey=479334790e5343abb9a3b43228f4b465'
    
    print("Api url", api_url)
    response = requests.get(api_url)
    data=response.json()
    if response.status_code == 200:
         return json.loads(response.content.decode('utf-8'))

         print(response.content.decode('utf-8'))
    else:
        return print('Something is wrong')

    for article in data:
        print("Title : ", article["title"])
        print("decription : ",'article["description"]')
        print("url: ",article["url"])
    

get_headlines()
