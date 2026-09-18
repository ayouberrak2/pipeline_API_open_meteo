import sys

sys.path.append("/opt/airflow")


from datetime import datetime

from src.extract.app import extract
from src.transform.siler_transform import transforme_silver
from src.transform.gold_transforme import transforme_gold

from src.load.app import load_data

from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator


with DAG(
    dag_id = "wheater_pipeline",
    start_date = datetime(2026,9,18),
    schedule = None,
    catchup = False
) as dag :
    extract_task = PythonOperator(
        task_id = "extract",
        python_callable = extract
    )

    transform_silver_task = PythonOperator(
        task_id = "silver",
        python_callable = transforme_silver
    )

    transform_gold_task  = PythonOperator(
        task_id = "gold",
        python_callable = transforme_gold
    )

    load_task = PythonOperator(
        task_id = "load",
        python_callable = load_data
    )

    extract_task >> transform_silver_task >> transform_gold_task >> load_task