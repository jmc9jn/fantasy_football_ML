#The purpose of this script is to gather play stats using the nfl_data_py api

import pandas as pd
import nfl_data_py as nfl

class getPlayerStatsAPI:
    def __init__(self, range_start, range_end):
        self.date_range = [*range(range_start, range_end)]

    def get_all_stats(self):
        self.df = nfl.import_weekly_data(self.date_range)
        self.df.to_csv('/Users/jungchoi/fantasy_football_ML/data/raw/all_position_stats.csv')

    def get_positional_stats(self, position):
        #Get all columns for QBs
        qb_columns = ['player_display_name', 'recent_team', 'season', 'week', 'season_type','opponent_team','rushing_yards','completions',
                      'attempts','passing_yards','passing_tds', 'interceptions', 'sacks', 'sack_fumbles','sack_fumbles_lost', 'passing_air_yards']

        #Get all columns for RBs, WRs, and TEs
        non_qb_columns = ['player_display_name', 'recent_team', 'season', 'week', 'season_type','opponent_team','carries','rushing_yards',
                                 'rushing_tds', 'receptions','targets','receiving_yards', 'receiving_tds', 'receiving_air_yards', 'receiving_yards_after_catch',
                          'receiving_epa', 'target_share','air_yards_share','wopr']


        if position == 'QB':
            quarterback_stats = self.df.loc[self.df.position == 'QB', qb_columns]
            quarterback_stats.to_csv('/Users/jungchoi/fantasy_football_ML/data/raw/quarterback_stats.csv')

        # Filter for all wide receiver data
        elif position == 'WR':
            wide_receiver_stats = self.df.loc[self.df.position == 'WR', non_qb_columns]
            wide_receiver_stats.to_csv('/Users/jungchoi/fantasy_football_ML/data/raw/wide_receiver_stats.csv')

        #Filter for all running back data
        elif position == 'RB':
            running_back_stats = self.df.loc[self.df.position == 'RB', non_qb_columns]
            running_back_stats.to_csv('/Users/jungchoi/fantasy_football_ML/data/raw/running_back_stats.csv')

        #Filter for all tight end data
        elif position == 'TE':
            tight_end_stats = self.df.loc[self.df.position == 'TE', non_qb_columns]
            tight_end_stats.to_csv('/Users/jungchoi/fantasy_football_ML/data/raw/tight_end_stats.csv')

