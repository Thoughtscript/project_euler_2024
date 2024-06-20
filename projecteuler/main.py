from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from router import project_euler

app = FastAPI() 

app.include_router(project_euler.api)
app.mount("/public", StaticFiles(directory="public"), name="public")