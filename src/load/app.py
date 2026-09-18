import pandas as pd
import psycopg2

def load_data():
    df = pd.read_csv("data/gold/final_data.csv")


    conn = psycopg2.connect(
        host="postgres",
        database="pipeline_api_open_meteo",
        user = "root",
        password = "12341234",
        port=5432
        )

    cursor = conn.cursor()

    for _, row in df.iterrows():

        cursor.execute(
            "SELECT id FROM city WHERE name = %s",(row["city"],)
        )

        res = cursor.fetchone()

        if res :
            city_id = res[0]
        else :
            cursor.execute(
                "INSERT INTO city (" \
                "name,latitude,longitude" \
                ")" \
                "VALUES (%s,%s,%s)" \
                "RETURNING id",
                (
                    row["city"],
                    row["latitude"],
                    row["longitude"]
                )
            )

            city_id = cursor.fetchone()[0]

        cursor.execute(
            
            "INSERT INTO weather (" \
            "city_id,date,temperature_max,temperature_min,temperature_moyenne,precipitation,probabilite_pluie,vent,risk_score,risk_level,meteo_code" \
            ")" \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s)" \
            "RETURNING id"
            ,
            (
                city_id,
                row["date"],
                row["temperature_max"],
                row["temperature_min"],
                row["temperature_moyenne"],
                row["precipitation"],
                row["probabilite_pluie"],
                row["vent"],
                row["risk_score"],
                row["risk_level"],
                row["meteo_code"]
            )
        )

    conn.commit()
    cursor.close()
    conn.close()



if __name__ == "__main__":
    load_data()