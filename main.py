#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 28 11:08:42 2019

@author: harundemir
"""

import requests
from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')

def ChuckNorris():
    response = requests.get('https://api.chucknorris.io/jokes/random')

    responseCode = response.status_code
    responseJoke = response.json()['value']

    all_freq = {} 
  
    for i in responseJoke: 
        if i in all_freq: 
            all_freq[i] += 1
        else: 
            all_freq[i] = 1

    counts = str(all_freq)
    result = responseJoke + '                       Counts: ' + counts
    return result

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run()
