from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "status": "Active and Secure",
        "message": "Aegis Production System Test Live!"
    }