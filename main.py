from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks data from the provided JSON file
with open("marks.json") as f:
    marks_data = json.load(f)

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    # Return marks in the same order as names given
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}
