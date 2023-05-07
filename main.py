from fastapi import FastAPI, Body
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

# Parámetros query, cuando no se indica en la ruta, si no como parámetro
# @app.get("/movies/", tags=["movies"])
# def get_movies_by_category(category: str, year: int):
#     return category, year

# Parámetros query, filtrando por categoría
@app.get("/movies/", tags=["movies"])
def get_movies_by_category(category: str, year:int):
    return [ item for item in movies if item["category"] == category]

# Método POST
@app.post("/movies", tags=["movies"])
def create_movie(id: int = Body(), tittle: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({ # Insertar datos
        "id": id,
        "tittle": tittle,
        "overview": overview,
        "year": year,
        "rating": rating,
        "category": category
    })
    return movies
