from fastapi import FastAPI
import sqlite3 as sql

app = FastAPI()

@app.get("/films")
def les_films():
    connexion = sql.connect("films.db")
    films = connexion.execute("SELECT * FROM films").fetchall()
    connexion.close()
    print('films:', films)

    liste = []
    for film in films:
        liste.append({
            'id': film[0],
            'titre': film[1],
            'annee': film[2],
            'note': film[3]
        })
    return liste

@app.get('/films/{id}')
def recup_film(id: int):
    connexion = sql.connect("films.db")
    film = connexion.execute('SELECT * FROM films WHERE id = ?', (id,)).fetchall()

    if film is None:
        return {'message': 'film non trouvé'}