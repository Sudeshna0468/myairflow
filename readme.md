1. instalar docker
2. criar pasta vazia myairflow
3. criar pasta airflow-docker  
    - mkdir airflow-docker

4. create docker-compose from https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
    - mkdir dags 
    - mkdir logs 
    - mkdir plugins

5. starting airflow
    - cd airflow-docker
    - docker-compose up airflow-init
    - docker-compose up

