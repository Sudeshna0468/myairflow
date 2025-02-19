from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'example_postgres',
    default_args=default_args,
    schedule_interval='@daily',
)

# Task to read from the database
read_task = PostgresOperator(
    task_id='read_from_db',
    postgres_conn_id='your_postgres_connection',
    sql='SELECT * FROM your_table;',
    dag=dag,
)

# Task to write to the database
write_task = PostgresOperator(
    task_id='write_to_db',
    postgres_conn_id='your_postgres_connection',
    sql='''
    INSERT INTO your_table (column1, column2)
    VALUES ('value1', 'value2');
    ''',
    dag=dag,
)

read_task >> write_task