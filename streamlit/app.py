import streamlit as st
import psycopg2
import pandas as pd


conn = psycopg2.connect(
    host="postgres",
    port="5432",
    database="pipeline_api_open_meteo",
    user="root",
    password="12341234"
)


query = """
SELECT
    c.name AS city,
    w.date,
    w.temperature_max,
    w.temperature_min,
    w.temperature_moyenne,
    w.precipitation,
    w.probabilite_pluie,
    w.vent,
    meteo_code,
    w.risk_score,
    w.risk_level
FROM weather w
JOIN city c
    ON w.city_id = c.id
ORDER BY w.date;
"""

cursor = conn.cursor()

cursor.execute(query)

res = cursor.fetchall()

columns = [desc[0] for desc in cursor.description]

cursor.close()
conn.close()

df = pd.DataFrame(res, columns=columns)

st.write(df)