import pandas as pd
import nfl_data_py as nfl

# Pull api from 2010 to 2023 gamne logs
seasons = list(range(2010, 2024))
df = nfl.import_weekly_data(seasons)

#Export raw game logs in csv format
df.to_csv('/Users/jungchoi/PycharmProjects/PythonProject1/data/raw/player_game_logs.csv')

#Get all columns for RBS, WRS, and TES
non_qb_columns = ['player_display_name', 'recent_team', 'season', 'week', 'season_type','opponent_team','rushing_yards',
                         'rushing_tds', 'receptions','targets','receiving_yards', 'receiving_tds', 'receiving_air_yards', 'receiving_yards_after_catch',
                  'receiving_epa', 'target_share','air_yards_share','wopr']

#Filter for all wide receiver data
wide_receiver_stats = df.loc[df.position == 'WR', non_qb_columns]
wide_receiver_stats.to_csv('/Users/jungchoi/PycharmProjects/PythonProject1/data/processed/wide_receiver_stats.csv')

#Filter for all running back data
running_back_stats = df.loc[df.position == 'RB', non_qb_columns]
running_back_stats.to_csv('/Users/jungchoi/PycharmProjects/PythonProject1/data/processed/running_back_stats.csv')

#Filter for all tight end data
tight_end_stats = df.loc[df.position == 'TE', non_qb_columns]
tight_end_stats.to_csv('/Users/jungchoi/PycharmProjects/PythonProject1/data/processed/tight_end_stats.csv')
