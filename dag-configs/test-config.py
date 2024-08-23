from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def generate_pascals_triangle():
    def generate(levels):
        triangle = [[1]]
        for i in range(1, levels):
            row = [1]
            for j in range(1, i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        return triangle

    pascals_triangle = generate(10)
    for row in pascals_triangle:
        print(' '.join(map(str, row)))

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'pascal',
    default_args=default_args,
    description='DAG для генерации треугольника Паскаля',
    schedule_interval='44 11 * * *',
)

t1 = PythonOperator(
    task_id='generate_pascals_triangle',
    python_callable=generate_pascals_triangle,
    dag=dag,
)
