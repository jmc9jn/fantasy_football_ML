from api.get_game_location_data import gameLocationAPI

if __name__ == '__main__':
    api = gameLocationAPI(2010, 2024)
    api.get_schedule()
