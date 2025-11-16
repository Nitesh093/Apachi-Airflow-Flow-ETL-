from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

# Import functions from task files
from tasks.extract import extract
from tasks.transform import transform
from tasks.load import load

with DAG(
    dag_id="simple_etl_dag",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["etl", "example"]
) as dag:

    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    # Set dependencies
    extract_task >> transform_task >> load_task