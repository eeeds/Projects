#import the libraries
from datetime import timedelta 
#Import DAG
from airflow import DAG
#Import operators
from airflow.operators.bash_operator import BashOperator
#For scheduling
from airflow.utils.dates import days_ago
#Create the DAG Arguments block.
default_args = {
    'owner': 'Esteban Encina',
    'start_date': days_ago(0),
    'email': ['encinaesteban@hola.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

#Defining the Acces-Logs DAG
dag = DAG(
    'ETL-Server-Access-Log-Processing',
    default_args=default_args,
    description='DAG from exercise',
    schedule_interval=timedelta(days=1),
)
#Creating a download task
download = BashOperator(
    task_id='download',
    bash_command='wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Apache%20Airflow/Build%20a%20DAG%20using%20Airflow/web-server-access-log.txt',
    dag=dag,
)
#Extract task

extract = BashOperator(
    task_id = 'extract',
    bash_command = 'cut -d"#" -f1,4 web-server-access-log.txt > extracted_data.txt'
    dag = dag,
)

#Transform task 

transform = BashOperator(
    task_id = 'transform',
    bash_command = 'tr "[a-z]" "[A-Z]" < extracted_data.txt > capitalized.txt',
    dag = dag,
)

#Create the load task 
load = BashOperator(
    task_id = 'load',
    bash_command = 'zip log.zip capitalized.txt',
    dag = dag,
)
#Create the task pipeline block
download >> extract >> transform >> load 
