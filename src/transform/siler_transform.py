import pandas as pd
from pathlib import Path
import json


def transforme_silver():
    def reorganise(df):
        df["latitude"] = pd.to_numeric( df["latitude"], errors="coerce" ) 
        df["longitude"] = pd.to_numeric( df["longitude"], errors="coerce" )
        df["temperature_max"] = pd.to_numeric( df["temperature_max"], errors="coerce" )
        df["temperature_min"] = pd.to_numeric( df["temperature_min"], errors="coerce" )
        df["precipitation_sum"] = pd.to_numeric( df["precipitation_sum"], errors="coerce" )
        df["precipitation_probability_max"] = pd.to_numeric( df["precipitation_probability_max"], errors="coerce" )
        df["wind_speed_max"] = pd.to_numeric( df["wind_speed_max"], errors="coerce" )
        df["wind_gusts_max"] = pd.to_numeric( df["wind_gusts_max"], errors="coerce" )
        df["weather_code"] = pd.to_numeric( df["weather_code"], errors="coerce" )
        df["date"] = pd.to_datetime(df["date"],errors="coerce")
        return df 


    def merge_dataframe(df_cities,meteo_file):

        dataframes = []
        for file in meteo_file.glob("*.json"):
            # print(file)
            with open(file,"r",encoding="utf-8") as f:
                meteo = json.load(f)

            df = pd.DataFrame(meteo)
            dataframes.append(df)

        df_f = pd.concat(
            dataframes,
            ignore_index=True
        )

        df_final = pd.merge(
            df_f,
            df_cities,
            on="city",
            how="left"
        )

        df_final = reorganise(df_final)

        df_final = df_final.drop_duplicates(
            subset=["city","date"]
        )

        df_final.to_csv("data/silver/meteo.csv", index=False)

        return df_final


    df_cites= pd.read_csv("data/bronze/cities.csv")
    meteo_file= Path("data/bronze/weather")

    merge_dataframe(df_cities=df_cites , meteo_file=meteo_file)


if __name__ =="__main__":
    transforme_silver()