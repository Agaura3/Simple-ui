from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ✅ DB imports (ADD)
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

app = FastAPI()

# ✅ CORS (as it is)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ DB connection (ADD)
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# (optional temporary check)
print("DB URL loaded:", DATABASE_URL is not None)

# ✅ existing routes (NO CHANGE)
@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/check")
def check(num1: int, num2: int):
    if num1 > num2:
        return {"status": "greater"}
    elif num1 < num2:
        return {"status": "less"}
    else:
        return {"status": "equal"}
