from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import json	# read json format
import requests	#make get request
import pyodbc  # run SQL Queries
import textwrap

class ActionWeather(Action):
    def name(self):
        return 'action_weather'
    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot('GPE')
        #if tracker.get_slot('STATE') == None:
        #    state = ''
        #else:
        #    state = tracker.get_slot('STATE')
        location = "'" + city + "'"      
        url = 'https://query.yahooapis.com/v1/public/yql?q=select* from weather.forecast where woeid in (select woeid from geo.places(1) where text=' + location + ')'
        response = requests.get(url, headers={"Accept": "application/json"})
        data = response.json()
        s = requests.Session()
        s.close

        weather_location = data['query']['results']['channel']['location']
        city = weather_location['city']
        region = weather_location['region']
        country = weather_location['country']
        weather = data['query']['results']['channel']['item']['condition']
        temp = weather['temp']
        text = weather['text']
        date = weather['date']
        response = """In {}, {}, {}... It is {} degrees and {} as of {} """.format(city, region, country, temp, text, date)
        dispatcher.utter_message(response)
        return [SlotSet('CITY', city)]
