from datetime import datetime
from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from airflow.models.param import Param

with DAG(
    "docker_sample",  # DAG名
    start_date=datetime(2023, 1, 1),  # DAGの開始時刻
    schedule=None,  # DAGをスケジュール実行しない設定
    catchup=False,
    params={
        "command": Param(":", type="string"),  # コンテナに渡すコマンド
        "env_ID": Param("hoge", type="string"),  # コンテナに渡す環境変数
    },
    tags=["docker"],  # タグ
) as dag:
    docker_task = DockerOperator(
        task_id="docker_command_sleep",  # タスク名
        priority_weight=10,  # タスクの実行優先度
        image="nginx",  # Dockerイメージ名
        api_version="auto",
        auto_remove="True",  # 実行後にコンテナを削除するか（True/never）
        command="{{params.command}}",  # コンテナに渡すコマンド
        docker_url="unix://var/run/docker.sock",  # DooDのために必要な設定
        network_mode="bridge",  # コンテナのネットワーク設定
        pool="SampleTaskPool",  # コンテナの所属先Pool名
        environment={"ID": "{{params.env_ID}}"},  # コンテナに渡す環境変数
    )
