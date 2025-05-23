from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json
from pathlib import Path

app = FastAPI()

# Enable CORS for all origins and methods
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load marks.json once at startup
MARKS_PATH = Path(__file__).parent / "marks.json"
with open(MARKS_PATH, "r") as f:
    marks_data = json.load(f)

@app.get("/")
def root():
    return {"message": "Use /api?name=... to get marks."}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    # Search for marks by name in the array
    result = []
    for n in name:
        found = next(
            (item["marks"] for item in marks_data if item["name"] == n),
            None
        )
        result.append(found)
    return {"marks": result}
@app.get("/favicon.ico")
def favicon():
    return ""
