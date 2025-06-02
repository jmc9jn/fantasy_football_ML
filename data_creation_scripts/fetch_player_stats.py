from api.get_player_stats import getPlayerStatsAPI

def get_player_stats(range_start, range_end):
    api = getPlayerStatsAPI(range_start, range_end)
    api.get_all_stats()

    return api

if __name__ == "__main__":
    api = get_player_stats(2010, 2024)
    positions = ['QB','RB','WR','TE']
    for position in positions:
        api.get_positional_stats(position)