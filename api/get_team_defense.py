#The purpose of this script is to gather  team defense stats

import pandas as pd
import nfl_data_py as nfl

class getTeamDefenseStatsAPI:
    def __init__(self, range_start, range_end):
        self.date_range = [*range(range_start, range_end)]

    def get_defense_stats(self):
        df = nfl.import_weekly_data(self.date_range)

        relevant_positions = ['QB','RB','WR','TE', 'FB']
        relevant_columns = ['opponent_team', 'season','week','completions','attempts','passing_yards','passing_tds','interceptions', 'sacks','sack_fumbles',
                            'passing_air_yards','passing_yards_after_catch','carries','rushing_yards','rushing_tds',
                            'rushing_fumbles', 'rushing_first_downs','receptions','targets','receiving_yards','receiving_tds','receiving_fumbles',
                            'receiving_air_yards','receiving_yards_after_catch']
        filtered_df = df.loc[df.position.isin(relevant_positions), relevant_columns]
        grouped_df = filtered_df.groupby(['opponent_team','season','week'])['completions','attempts','passing_yards','passing_tds','interceptions', 'sacks', 'sack_fumbles',
                            'passing_air_yards','passing_yards_after_catch','carries','rushing_yards','rushing_tds',
                            'rushing_fumbles',  'rushing_first_downs','receptions','targets','receiving_yards','receiving_tds','receiving_fumbles',
                            'receiving_air_yards','receiving_yards_after_catch'].sum().reset_index()

        grouped_df.rename(columns = {
            'completions':'completions_allowed',
            'passing_yards':'passing_yards_allowed',
            'passing_tds':'passing_tds_allowed',
            'passing_air_yards':'passing_air_yards_allowed',
            'passing_yards_after_catch':'passing_yards_after_catch_allowed',
            'rushing_yards':'rushing_yards_allowed',
            'rushing_tds':'rushing_tds_allowed',
            'receptions':'receptions_allowed',
            'receiving_yards':'receiving_yards_allowed',
            'receiving_tds':'receiving_tds_allowed',
            'receiving_air_yards':'receiving_air_yards_allowed',
            'sack_fumbles':'sack_fumbles_forced',
            'rushing_fumbles':'rushing_fumbles_forced',
            'receiving_fumbles':'receiving_fumbles_forced',
        }, inplace = True)

        grouped_df['completion_percentage_allowed'] = grouped_df['completions_allowed'] / grouped_df['attempts']
        grouped_df['rush_per_attempt_allowed'] = grouped_df['rushing_yards_allowed'] / grouped_df['carries']
        grouped_df['yards_per_catch_allowed'] = grouped_df['receiving_yards_allowed'] / grouped_df['completions_allowed']

        grouped_df.drop(['attempts','carries','targets'], axis=1, inplace=True)

        return grouped_df



