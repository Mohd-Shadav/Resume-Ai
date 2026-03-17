from fastapi import FastAPI
from mangum import Mangum

from api.database import *
from api.models import *

app = FastAPI(title="Resume AI Backend")

@app.get("/")
def home():
    return {"message": "Resume AI backend running 🚀"}

# REQUIRED for Vercel
handler = Mangum(app)