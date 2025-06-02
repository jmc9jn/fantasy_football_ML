#The purpose of this script is to gather game day conditions data using the visualcrossing api

import requests
import json
import pandas as pd

class WeatherAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

    #Create a function to call visual crossing api to gather weather information from game day
    def get_weather_visualcrossing(self, location, date, time):
        datetime_str = f"{date}T{time}"
        url = f"{self.base_url}/{location}/{datetime_str}"

        params = {
            "key": self.api_key,
            "unitGroup": "us",
            "include": "hours"
        }

        try:
            res = requests.get(url, params=params)
            data = res.json()

            data_dict = {'conditions': data['days'][0]['conditions'],
                         'precipitation': data['days'][0]['precip'],
                         'snow_depth': data['days'][0]['snowdepth'],
                         'temperature': data['days'][0]['temp'],
                         'windspeed': data['days'][0]['windspeed']}

            return data_dict

        except Exception as e:
            print(f"[ERROR] Failed for {location} at {datetime_str}: {e}")
            return None
