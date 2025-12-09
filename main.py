from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/run")
def run_script():

    try:
        # Pokreće tvoju Python skriptu
        result = subprocess.run(
            ["python3", "/data/valid.py"], 
            capture_output=True, 
            text=True
        )
        
        return {
            "success": True,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
