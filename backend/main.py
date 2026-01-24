from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
