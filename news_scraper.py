#!/usr/local/bin/python3

import requests

def main(): 
	#sources = ['the-wall-street-journal']
	url = ('https://newsapi.org/v2/top-headlines?'
		'sources=the-wall-street-journal&'
		'apiKey=6852f94cb1ed44f98e6845a2b21c28c9')
	response = requests.get(url)
	print(response.json())

if __name__=='__main__':
	main()