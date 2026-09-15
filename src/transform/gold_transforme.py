import pandas as pd
import conditions


df = pd.read_csv("data/silver/meteo.csv")

df["date"] = pd.to_datetime(df["date"])


def weather_risk_score(row):
    temp = conditions.temperature_category(row["temperature_max"])
    pre = conditions.precipitation_category(row["precipitation_sum"])
    wind = conditions.wind_category(row["wind_speed_max"])
    pre_pro = conditions.precipitation_probability(row["precipitation_probability_max"])

    return temp + pre + wind + pre_pro


df["temperature_moyenne"] = (
    df["temperature_max"] + df["temperature_min"]
)/2 

df["risk_score"] = df.apply(
    weather_risk_score,
    axis=1
)


df["risk_level"] = df["risk_score"].apply(conditions.risk_level)

df_gold = df[
    [
        "city",
        "latitude",
        "longitude",
        "date",
        "temperature_max",
        "temperature_min",
        "temperature_moyenne",
        "precipitation_sum",
        "precipitation_probability_max",
        "wind_speed_max",
        "weather_code",
        "risk_score",
        "risk_level"
    ]
].copy()


df_gold = df_gold.rename(columns={ 
    "precipitation_sum": "precipitation", 
    "precipitation_probability_max": "probabilite_pluie", 
    "wind_speed_max": "vent", 
    "weather_code": "meteo_code" 
    })


df_gold.to_csv("data/gold/final_data.csv")

# print(df)