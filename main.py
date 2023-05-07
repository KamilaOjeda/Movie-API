from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi primera app con FastAPI"
app.version = "0.0.1"

# Creamos la clase/esquema que va a contener tod la info de cada película
class Movie(BaseModel):
    # id: int | None = None ## None es para indicar que puede ser opcional, sin embargo hay otra forma: tiping.
    id: Optional[int] = None
    tittle: str
    overview: str
    year: int
    rating: float
    category: str

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
# def create_movie(id: int = Body(), tittle: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
def create_movie(movie: Movie): ## En vez de poner cada elemento del body, utilizamos este atajo
    movies.append(movie) # Insertar datos
    return movies

# # Método PUT, como parámetro de ruta
# @app.put("/movies/{id}", tags=["movies"])
# def update_movie(id: int, tittle: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
#     for item in movies:
#         if item["id"] == id:
#             item["tittle"] = tittle,
#             item["overview"] = overview,
#             item["year"] = year,
#             item["rating"] = rating, 
#             item["category"] = category
#             return movies

# Método PUT, como parámetro de ruta
@app.put("/movies/{id}", tags=["movies"])
def update_movie(id: int, movie: Movie):
    for item in movies:
        if item["id"] == id:
            item["tittle"] = movie.tittle
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return movies

# Método DELETE, como parámetro de ruta
@app.delete("/movies/{id}", tags=["movies"])
def update_movie(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies