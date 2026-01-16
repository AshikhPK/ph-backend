from fastapi import FastAPI

app = FastAPI()

# global storage
latest_ph = {"value": None}

@app.get("/")
def root():
    return {"status": "Backend is running"}

@app.get("/api/ph")
def get_ph():
    return latest_ph

@app.get("/api/ph/update")
def update_ph(ph: float):
    latest_ph["value"] = ph
    return {"status": "updated", "value": ph}
