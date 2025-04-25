from fastapi import FastAPI

app = FastAPI()

@app.get("/api/hello")
def hello_wolrd():
    return {"Hello": "World"}