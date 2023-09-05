from datetime import datetime
from airflow import DAG
from airflow.models.param import Param
from airflow.providers.http.operators.http import SimpleHttpOperator

with DAG(
    "http_sample",  # DAG名
    start_date=datetime(2023, 1, 1),  # DAGの開始時刻
    schedule=None,  # DAGをスケジュール実行しない設定
    catchup=False,
    tags=["http"],  # タグ
    params={"intparam": Param(60, type="integer", minimum=10)},
) as dag:
    SimpleHttpOperator(
        task_id="http_task",  # タスク名
        http_conn_id="",  # HTTPリクエスト送信先のURL（endpointとセットで利用）
        endpoint="http://localhost:3000/api",  # HTTPリクエスト送信先のURL
        data='{"param": "{{params.intparam}}"}',  # POSTデータ
        log_response=True,  # Airflow WebUI上にHTTPレスポンスをログとして表示する
        headers={"Content-Type": "application/json"},
    )
