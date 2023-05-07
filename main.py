from fastapi import FastAPI

app = FastAPI()
app.title = "Mi primera app con FastAPI"
app.version = "0.0.1"

@app.get('/')
def message():
    return "Hello world!"