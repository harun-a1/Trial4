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

response = requests.get('https://api.chucknorris.io/jokes/random')

responseCode = response.status_code
responseJoke = response.json()['value']

all_freq = {} 
  
for i in responseJoke: 
    if i in all_freq: 
        all_freq[i] += 1
    else: 
        all_freq[i] = 1
        

Joke = responseJoke
result = str(all_freq)
print(Joke + ' \n Counts: ' + result)
