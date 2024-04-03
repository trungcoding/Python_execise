import time
from datetime import datetime
from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.mysql.hooks.mysql import MySqlHook
from airflow.hooks.base import BaseHook
from sqlalchemy import create_engine

def get_data_from_mysql():
    hook = MySqlHook(mysql_conn_id="mysql")
    sql = "SELECT * FROM peopleData"
    df = hook.get_pandas_df(sql)
    print(df)
    tbl = df.to_dict('dict')
    return tbl

def load_data_to_postgres(**kwargs):
    ti = kwargs['ti']
    tbl = ti.xcom_pull(task_ids='get_data_from_mysql_task')
    
    conn = BaseHook.get_connection("postgresql")
    engine = create_engine(f'postgresql://{conn.login}:{conn.password}@{conn.host}:{conn.port}/{conn.schema}')
    all_tbl_name = []
    start_time = time.time()
    rows_imported = 0
    
    for k, v in tbl.items():
        all_tbl_name.append(k)
        sql = f'select * FROM {v}'
        hook = MySqlHook(mysql_conn_id="mysql")
        df = hook.get_pandas_df(sql)
        print(f'importing rows {rows_imported} to {rows_imported + len(df)}... for table {k}')
        df.to_sql(f'src_{k}', engine, if_exists='replace', index=False)
        rows_imported += len(df)
        print(f'Done. {str(round(time.time() - start_time, 2))} total seconds elapsed')
    
    print("Data imported successful")
    return all_tbl_name

with DAG(dag_id="product_etl_dag", schedule="0 9 * * *", start_date=datetime(2022, 3, 5), catchup=False) as dag:
    get_data_from_mysql_task = PythonOperator(
        task_id='get_data_from_mysql_task',
        python_callable=get_data_from_mysql,
    )
    
    load_data_to_postgres_task = PythonOperator(
        task_id='load_data_to_postgres_task',
        python_callable=load_data_to_postgres
    )

get_data_from_mysql_task >> load_data_to_postgres_task

