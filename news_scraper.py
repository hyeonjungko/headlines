#!/usr/local/bin/python3
import requests

# TODO: schedule the job to execute every 24hrs w/ schedule library
# TODO: implement email method w/ smtplib, email

def display(data):
    # print(data['articles'])
    urls = []

    # Print title and description of each article
    for article in data['articles']:
        print(article['title'])
        urls.append(article['url'])
        print(article['description'])
        print('')

    # Print article links
    for url in urls:
        print(url)


def get_articles():
    url = ('https://newsapi.org/v2/top-headlines?'
            'sources=the-wall-street-journal&'
            'apiKey=6852f94cb1ed44f98e6845a2b21c28c9')
    response = requests.get(url)
    data = response.json()
    display(data)


if __name__ == '__main__':
    # TODO: implement sources & country option
    # sources = ['the-wall-street-journal&', ...]
    # get_article(sources)
    get_articles()
