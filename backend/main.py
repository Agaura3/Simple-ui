from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# 🔹 FastAPI app
app = FastAPI()

# 🔹 CORS (frontend ke liye)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 DATABASE CONNECTION (DIRECT – no env variable)
DATABASE_URL = "postgresql://simple_ui_db_user:V6kVyXfH2n4WqCuYHhAIWezfpDaUuNI4@dpg-d5sgh6v18n1s739o8g2g-a.oregon-postgres.render.com:5432/simple_ui_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# 🔹 Root route
@app.get("/")
def root():
    return {"message": "API is running"}

# 🔹 Existing check route (as it is)
@app.get("/check")
def check(num1: int, num2: int):
    if num1 > num2:
        return {"status": "greater"}
    elif num1 < num2:
        return {"status": "less"}
    else:
        return {"status": "equal"}

# 🔹 USERS API (DB se data read karega)
@app.get("/users")
def get_users():
    db = SessionLocal()
    result = db.execute(text("SELECT * FROM users"))
    users = result.mappings().all()
    db.close()
    return users
