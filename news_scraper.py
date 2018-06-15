#!/usr/local/bin/python3
import requests


def display(data):
    #print(data['articles'])

    for article in data['articles']:
        print(article['title'])
        print(article['url'])
        print(article['description'])
        print('')

def get_articles(): 
    url = ('https://newsapi.org/v2/top-headlines?'
            'sources=the-wall-street-journal&'
            'apiKey=6852f94cb1ed44f98e6845a2b21c28c9')
    response = requests.get(url)
    data = response.json()
    display(data)

if __name__=='__main__':
    #sources = ['the-wall-street-journal&', ...]
    #get_article(sources)
    get_articles()
