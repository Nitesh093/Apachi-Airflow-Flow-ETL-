# def load():
#     print('task is loaded in postgres')




# tasks/load.py
import psycopg2
import os
import pandas as pd
from psycopg2.extras import execute_values

def load(**kwargs):
    """
    Load transformed data into Postgres table `model_list` using bulk insert.
    Much faster than row-by-row inserts.
    """
    # Pull transformed data from XCom
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(key='transformed_data', task_ids='transform')

    if not transformed_data:
        print("No data to load.")
        return "No data to load"

    # Convert to DataFrame
    df = pd.DataFrame(transformed_data)

    # Database connection parameters
    DB_HOST = os.getenv("DB_HOST")
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_PORT = os.getenv("DB_PORT")

    try:
        # Connect to Postgres
        conn = psycopg2.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            dbname=DB_NAME,
            port=DB_PORT
        )
        cursor = conn.cursor()

        # Generate insert query dynamically
        columns = df.columns.tolist()
        columns_str = ', '.join(f'"{col}"' for col in columns)
        insert_query = f'INSERT INTO model_list ({columns_str}) VALUES %s'

        # Convert DataFrame to list of tuples
        values = [tuple(row) for row in df.to_numpy()]

        # Bulk insert (super fast)
        execute_values(cursor, insert_query, values, page_size=1000)

        # Commit and close
        conn.commit()
        cursor.close()
        conn.close()

        print(f"✅ Successfully loaded {len(df)} rows into model_list table (bulk insert).")

    except Exception as e:
        print("❌ Error loading data into Postgres:", e)
        raise

    return "load completed"
