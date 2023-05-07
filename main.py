from fastapi import FastAPI
from fastapi.responses import HTMLResponse
app = FastAPI()
app.title = "Mi primera app con FastAPI"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
    "tittle": "Avatar",
    "overview": "En un exhuberante planeta llamado Pandora, viven los Na'vi",
    "year": "2009",
    "rating": "7.8",
    "category": "Acción"
    },
    {
        "id": 2,
    "tittle": "Avatar",
    "overview": "En un exhuberante planeta llamado Pandora, viven los Na'vi",
    "year": "2009",
    "rating": "7.8",
    "category": "Acción"
    }
]

# Método GET
@app.get('/', tags=["home"])
def message():
    return HTMLResponse("<h1>Hello world<h1>")

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies

# Parámetros de ruta
@app.get("/movies/{id}", tags=["movies"])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []