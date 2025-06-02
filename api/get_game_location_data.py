#The purpose of this script is to gather schedule data, mainly the location of the game using the nfl_data_py api

import nfl_data_py as nfl
import pandas as pd

class gameLocationAPI:
    def __init__(self, range_start, range_end):
        self.date_range = [*range(range_start, range_end)]

    # Load all game metadata from 2010–2023
    def get_schedule(self):
        games = nfl.import_schedules(self.date_range)

        # Keep only relevant columns
        game_cols = ['gameday', 'gametime', 'home_team']
        games = games.loc[:, game_cols]

        #Create a column for each home team's stadium location
        nfl_team_locations = {
            "ARI": "Glendale, AZ",
            "ATL": "Atlanta, GA",
            "BAL": "Baltimore, MD",
            "BUF": "Orchard Park, NY",
            "CAR": "Charlotte, NC",
            "CHI": "Chicago, IL",
            "CIN": "Cincinnati, OH",
            "CLE": "Cleveland, OH",
            "DAL": "Arlington, TX",
            "DEN": "Denver, CO",
            "DET": "Detroit, MI",
            "GB":  "Green Bay, WI",
            "HOU": "Houston, TX",
            "IND": "Indianapolis, IN",
            "JAX": "Jacksonville, FL",
            "KC":  "Kansas City, MO",
            "LV":  "Las Vegas, NV",
            "LAC": "Inglewood, CA",
            "LAR": "Inglewood, CA",
            "MIA": "Miami Gardens, FL",
            "MIN": "Minneapolis, MN",
            "NE":  "Foxborough, MA",
            "NO":  "New Orleans, LA",
            "NYG": "East Rutherford, NJ",
            "NYJ": "East Rutherford, NJ",
            "PHI": "Philadelphia, PA",
            "PIT": "Pittsburgh, PA",
            "SEA": "Seattle, WA",
            "SF":  "Santa Clara, CA",
            "TB":  "Tampa, FL",
            "TEN": "Nashville, TN",
            "WAS": "Landover, MD",
            'STL': "St. Louis, MO",
            'OAK': "Las Vegas, NV",
            'SD': "San Diego, CA",
            'LA': "Los Angeles, CA"
        }
        games['game_location'] = games['home_team'].map(nfl_team_locations)

        #Add :00 to the end of the game time to match weather api inputs
        games['gametime'] = games['gametime'].apply(lambda x: x + ":00")

        #Write the game schedule data to a csv file
        games.to_csv("/Users/jungchoi/fantasy_football_ML/data/raw/games_schedule.csv")

