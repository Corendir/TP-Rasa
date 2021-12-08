# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

import requests #pip install requests
import json

class Action_weather_location(Action):

    def name(self) -> Text:
        return "action_weather_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        location = tracker.get_slot('location')
        woeid_request_result = json.load(requests.get("https://www.metaweather.com/api/location/search/?query={0}".format(location)))
        woeid = woeid_request_result["woeid"]

        weather_request_result = json.load(requests.get("https://www.metaweather.com/api/location/{0}".format(woeid)))
        temperature = weather_request_result["the_temp"]
        humidity = weather_request_result["humidity"] * 100

        dispatcher.utter_message(text="The temperature in {0} is around {1} and the humidity is {2}%".format(weather_request_result, temperature, humidity))

        return []
        #return [weather_request_result, temperature, humidity]    
