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



df["weather_risk_score"] = df.apply(
    weather_risk_score,
    axis=1
)

df.to_csv("data/gold/final_data.csv")

# print(df)