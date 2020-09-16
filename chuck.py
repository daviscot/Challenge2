#!/usr/local/bin/python3

import json
import requests

url = 'https://api.chucknorris.io/jokes/random'

def get_chuck_joke(api):
    response = requests.get(api)
    return(json.loads(response.text))

if __name__ == '__main__':
    joke = get_chuck_joke(url)
    print(joke['value'])

#test 1234
