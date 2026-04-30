from fastapi import FastAPI
import sqlite3 as sql

app = FastAPI()

@app.get("/les_films")
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
    print(liste)