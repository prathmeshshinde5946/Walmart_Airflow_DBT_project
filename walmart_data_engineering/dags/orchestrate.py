from airflow.sdk import dag, task
from airflow.providers.standard.operators.bash import BashOperator
from databricks.sdk import WorkspaceClient
from databricks.sdk.service.jobs import RunLifeCycleState, RunResultState
import time
@dag(
        
)
def orchestrate():

    @task
    def ingest_cdc():
            ws = WorkspaceClient(
                host="<databricks host>",
                token="<databricks_token_id>"
                )

            job_trigger = ws.jobs.run_now(job_id="<Databricks_job_id>")

            while True:

                            job_run = ws.jobs.get_run(job_trigger.run_id)

                            # print(f"Job run Status: {job_run.state.life_cycle_state}, Result state:{job_run.state.result_state}")

                            if job_run.state.life_cycle_state in [RunLifeCycleState.TERMINATED, RunLifeCycleState.SKIPPED, RunLifeCycleState.INTERNAL_ERROR]:
                                if job_run.state.result_state == RunResultState.SUCCESS:
                                    print("Job completed successfully!")
                                    break 
                                else:
                                    raise Exception(f"Job failed with state: {job_run.state.result_state}")
                                    
                            time.sleep(5)  # Wait for 5 seconds before checking the 
                            
  
    @task.bash
    def remove_target_and_logs():
        return "rm -rf /opt/airflow/walmart_project/target && rm -rf /opt/airflow/walmart_project/logs"
    


    @task.bash
    def source_tranformation():
        # Run dbt from the mounted project directory.
        return "cd /opt/airflow/walmart_project && dbt source freshness"

    silver_technical = BashOperator( 
        task_id = 'silver_technical',
        bash_command='cd /opt/airflow/walmart_project && dbt run --select silver_t'
    )

    silver_technical_test = BashOperator(
            task_id = 'silver_technical_test',
            bash_command='cd /opt/airflow/walmart_project && dbt test --select silver_t'
        )

    silver_bussiness = BashOperator(
            task_id = 'silver_bussiness',
            bash_command='cd /opt/airflow/walmart_project && dbt run --select silver_b'
        )

    silver_bussiness_tests = BashOperator(
            task_id = 'silver_technical_tests',
            bash_command='cd /opt/airflow/walmart_project && dbt test --select silver_b'
        )

    gold_ephemeral = BashOperator(
        task_id= 'gold_ephemeral',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt run --select gold/ephemeral'
    )

    gold_dimensions = BashOperator(
        task_id='gold_dimensions',
        cwd='/opt/airflow/walmart_project',
        bash_command='dbt snapshot'
    )

    gold_facts = BashOperator(
            task_id='gold_facts',
            cwd='/opt/airflow/walmart_project',
            bash_command='dbt run --select gold/fact'
        )
    

    
    ingest_cdc() >> remove_target_and_logs() >> source_tranformation() >> silver_technical >> silver_technical_test >> silver_bussiness >> silver_bussiness_tests >> gold_ephemeral >> gold_dimensions >> gold_facts

orchestrate_dag = orchestrate()

    
