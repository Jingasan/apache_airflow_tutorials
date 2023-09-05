from datetime import datetime
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

with DAG(
    "bash_sample",  # DAG名
    start_date=datetime(2023, 1, 1),  # DAGの開始時刻
    schedule=None,  # DAGをスケジュール実行しない設定
    catchup=False,
    tags=["bash"],
) as dag:
    t1 = BashOperator(
        task_id="print_time1", bash_command="echo $(date '+%Y-%m-%d %H:%M:%S') start"
    )
    t2 = BashOperator(task_id="sleep", bash_command="sleep 30")
    t3 = BashOperator(
        task_id="print_time2", bash_command="echo $(date '+%Y-%m-%d %H:%M:%S') end."
    )
    t1 >> t2 >> t3
