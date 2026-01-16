from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

latest_ph = {"value": None}

class PHData(BaseModel):
    ph: float

@app.post("/api/ph")
def receive_ph(data: PHData):
    latest_ph["value"] = data.ph
    return {"status": "ok"}

@app.get("/api/ph")
def get_ph():
    return latest_ph
@app.get("/")
def root():
    return {"status": "Backend is running"}


