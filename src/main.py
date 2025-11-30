from fastapi import FastAPI

app = FastAPI()

@app.get("/verify")
def verify(lat: float, lon: float):
    return {
        "latitude": lat,
        "longitude": lon,
        "has_solar": True,
        "estimated_capacity_kw": 3.2,
        "message": "Demo output"
    }
