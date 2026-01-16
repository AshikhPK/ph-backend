from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

latest_ph = "EMPTY"

@app.get("/", response_class=PlainTextResponse)
def root():
    return "BACKEND ROOT OK"

@app.get("/api/ph", response_class=PlainTextResponse)
def get_ph():
    return f"PH VALUE = {latest_ph}"

@app.get("/api/ph/update", response_class=PlainTextResponse)
def update_ph(ph: float):
    global latest_ph
    latest_ph = str(ph)
    return f"UPDATED TO {latest_ph}"
