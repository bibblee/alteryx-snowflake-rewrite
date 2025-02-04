import subprocess
import os
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.snowflake.hooks.snowflake import SnowflakeHook
from datetime import datetime

from getpass import getpass
from configparser import ConfigParser

def run_dbt_model(dbt_model_name, **kwargs):
    """Runs a dbt model with dynamically generated profiles.yml"""

    profiles_dir = './config'

    try:
        result = subprocess.run(["dbt", "run", "--profiles-dir", profiles_dir, "--select", dbt_model_name],
                                check=True, capture_output=True, text=True)

        print("DBT Model Execution Output:")
        print(result.stdout)

        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing dbt model:")
        print(e.stderr)
        raise

# def run_fuzzy_match_script(dbt_model_name, **kwargs):
#     """Runs the existing fuzzy match script."""

#     profiles_dir = './config'
    
#     try:
#         result = subprocess.run(["dbt", "run", "--profiles-dir", profiles_dir, "--select", dbt_model_name],
#                                 check=True, capture_output=True, text=True)
#         print("Fuzzy Match Script Output:")
#         print(result.stdout)

#         return result.stdout
#     except subprocess.CalledProcessError as e:
#         print("Error executing fuzzy match script:")
#         print(e.stderr)
#         raise

dag = DAG(
    'airflow_pipeline_dag',
    default_args={'owner': 'airflow'},
    schedule_interval=None,
    start_date=datetime(2025, 1, 28),
)

task = PythonOperator(
    task_id='extract_data',
    python_callable=run_dbt_model,
    op_args=["pre_fuzzy_cleansed"],
    dag=dag,
)

task

# task1 = PythonOperator(
#     task_id='run_fuzzy_match',
#     python_callable=run_fuzzy_match_script,
#     op_args=["pre_fuzzy_result"],
#     dag=dag,
# )

# task1

# task >> task1
