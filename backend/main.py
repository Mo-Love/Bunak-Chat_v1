
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root(): return {"message": "Backend ready for omnichannel"}

@app.post("/chat")
def chat(data: dict): return {"response": f"Echo: {data}"}
