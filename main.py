from fastapi import FastAPI

# spt demo api

app = FastAPI()
movies = [{"title":"Demo movie", "year":"2001"}]

@app.get('/movies')
def movies_list():
  return movies

@app.post('/movies', status_code=201)
def add_movie(movie: dict):
  movies.append(movie)
