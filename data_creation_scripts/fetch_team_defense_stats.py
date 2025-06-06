#The purpose of this script is to call the api that gathers team defense stats

from api.get_team_defense import getTeamDefenseStatsAPI

def get_team_defense_stats(range_start, range_end):
    api = getTeamDefenseStatsAPI(range_start, range_end)
    api.get_defense_stats().to_csv('/Users/jungchoi/fantasy_football_ML/data/raw/team_defense.csv')

if __name__ == '__main__':
    get_team_defense_stats(2010, 2024)