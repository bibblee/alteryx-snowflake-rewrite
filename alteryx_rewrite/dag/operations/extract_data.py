# THIS IS A TEST TO STORE IT SEPARATELY LATELY


import subprocess

def run_dbt_model(**kwargs):
    """
    Runs the dbt model to select data from the SQL table and saves output to XCom.
    """
    try:
        result = subprocess.run([
            "dbt", "run", "--select", "your_dbt_model"
        ], check=True, capture_output=True, text=True)
        
        print("DBT Model Execution Output:")
        print(result.stdout)
        
        # Push result to XCom
        return result.stdout
    except subprocess.CalledProcessError as e:
        print("Error executing dbt model:")
        print(e.stderr)
        raise

if __name__ == "__main__":
    run_dbt_model()
