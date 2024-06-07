# instalar docker
# criar pasta vazia myairflow
# criar pasta airflow-docker  
mkdir airflow-docker

# create docker-compose from https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
mkdir dags 
mkdir logs 
mkdir plugins

docker-compose up airflow-init
docker-compose up

