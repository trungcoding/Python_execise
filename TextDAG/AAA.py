from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Định nghĩa một DAG với tên "my_dag"
dag = DAG(
    "my_dag",
    description="Chạy đoạn mã Python hàng ngày",
    schedule_interval="0 0 * * *",  # Chạy hàng ngày vào lúc 00:00 UTC
    start_date=datetime(2023, 1, 1),  # Ngày bắt đầu
    catchup=False,  # Không nắm bắt dữ liệu đã quá hạn
    default_args={
        "owner": "your_name",
        "depends_on_past": False,
        "retries": 1,
    },
)
def my_function():
    print("Hello from my Python script!")

if __name__ == "__main__":
    my_function()
# Định nghĩa một PythonOperator để thực thi đoạn mã Python
run_my_python_script = PythonOperator(
    task_id="run_my_python_script",
    python_callable=my_function,  # Gọi hàm my_function từ đoạn mã Python
    dag=dag,
)

# Xác định sự phụ thuộc giữa các tác vụ (nếu cần)
# ví dụ: run_my_python_script >> another_task

if __name__ == "__main__":
    dag.cli()
