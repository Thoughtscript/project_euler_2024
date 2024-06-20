from fastapi import APIRouter
import subprocess

api = APIRouter()

# /execute?problem=80
@api.get("/api/execute")
async def execute(problem):
    output = subprocess.getoutput("bash bin/run_solution.sh \"" + str(problem) + "\"")
    print(output)
    return output