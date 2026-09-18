import pandas as pd
import requests as rq
from pathlib import Path
import json
def extract():

    df_cities = pd.read_csv("data/bronze/cities.csv")

    df_cities =df_cities[[
        "city","lat","lng"
    ]]

    # print(df_cities)

    URL = "https://api.open-meteo.com/v1/forecast"


    def get_meteo(city,lat,lng):

        par = {
            "latitude": lat,
            "longitude": lng,
            "daily": [
                "temperature_2m_max",
                "temperature_2m_min",
                "precipitation_sum",
                "precipitation_probability_max",
                "wind_speed_10m_max",
                "wind_gusts_10m_max",
                "weather_code"
            ],
            "timezone": "Africa/Casablanca"
        }
        try: 
            response = rq.get(URL,params=par)
            response.raise_for_status()

            data = response.json()
            # print(data)

            daily = data["daily"]

            df_meteo = pd.DataFrame({
                "city": city,
                "latitude": lat,
                "longitude": lng,
                "date": daily["time"],
                "temperature_max": daily["temperature_2m_max"],
                "temperature_min": daily["temperature_2m_min"],
                "precipitation_sum": daily["precipitation_sum"],
                "precipitation_probability_max": daily["precipitation_probability_max"],
                "wind_speed_max": daily["wind_speed_10m_max"],
                "wind_gusts_max": daily["wind_gusts_10m_max"],
                "weather_code": daily["weather_code"]
            })


            folder_dir = Path("data/bronze/weather")
            folder_dir.mkdir(parents=True,exist_ok=True)

            file_dir = folder_dir/f"{city}.json"

            with open(file_dir,"w") as file :
                json.dump(df_meteo.to_dict(),file,ensure_ascii=False,indent=4)


            return df_meteo
        except :
            print("eror lors de appel de api")


    for _, row in df_cities.iterrows():
        # print(row)
        get_meteo(
            row["city"],
            row["lat"],
            row["lng"]
        )



if __name__ == "__main__":
    extract()



# print(__name__)