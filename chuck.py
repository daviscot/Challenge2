#!/usr/local/bin/python3

import json
import requests

url = 'https://api.chucknorris.io/jokes/random'

def get_chuck_joke(api):
    """
    Get a random joke from the Chuck Norris API and return the serial JSON
    :param api:
    :return:serial JSON
    """
    response = requests.get(api)
    return(json.loads(response.text))

if __name__ == '__main__':
    joke = get_chuck_joke(url)
    print(joke['value'])
