import datetime
import mysql.connector

from airflow import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="002_updatemysql",
    start_date=datetime.datetime(2021, 1, 1),
    schedule="@daily",
    catchup=False
):
    EmptyOperator(task_id="tarefa")

cnx = mysql.connector.connect(user='root', password='sgCzYueZ3nXRAaG',
                              host='host.docker.internal',
                              database='mariadbproject')

cursor = cnx.cursor()
query = ("update mariadbproject.tbproducts set active=1 where code=1;")
cursor.execute(query)

cursor.close()
cnx.commit()
cnx.close()
