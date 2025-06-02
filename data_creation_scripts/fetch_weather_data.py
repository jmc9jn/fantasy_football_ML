
import pandas as pd
from api.get_weather import WeatherAPI


def create_weather_enriched_dataset(schedule_path, output_path, api_key):
    api = WeatherAPI(api_key)
    df = pd.read_csv(schedule_path)

    weather_cols = ['conditions', 'precipitation', 'snow_depth', 'temperature', 'windspeed']
    for col in weather_cols:
        df[col] = None

    for i, row in df.iterrows():
        weather = api.get_weather_visualcrossing(row['game_location'], row['gameday'], row['gametime'])
        if weather:
            for col in weather_cols:
                df.at[i, col] = weather.get(col)

    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    create_weather_enriched_dataset(
        "/Users/jungchoi/fantasy_football_ML/data/raw/games_schedule.csv",
        "/Users/jungchoi/fantasy_football_ML/data/processed/schedule_with_weather.csv",
        "GU6QDTVPCJL6QJ6UNFCD9SV3K"
    )

