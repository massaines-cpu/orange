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
    film = connexion.execute('SELECT * FROM films WHERE id = ?', (id,)).fetchone()
    connexion.close()

    if film is None:
        return {'message': 'film non trouvé'}

    return {
        'id': film[0],
        'titre': film[1],
        'annee': film[2],
        'note': film[3]
    }

@app.post('/films')
def create_film(titre:str, annee:int, note:float):
    connexion = sql.connect("films.db")
    cursor = connexion.execute(
        'INSERT INTO films (titre, annee, note) VALUES (?, ?, ?)', (titre, annee, note)
    )
    connexion.commit()
    connexion.close()

    return {'message': 'ok', 'id': cursor.lastrowid}

@app.put('/films/{id}')
def modif_film(id:int, titre:str, annee:int, note:float):
    connexion = sql.connect("films.db")
    cursor = connexion.execute('UPDATE films SET titre = ?, annee = ?, note = ? WHERE id = ?',
                               (titre, annee, note, id)
                               )
    connexion.commit()
    connexion.close()
    return {'message': 'ok maj'}

@app.delete('/films/{id}')
def delete_film(id:int):
    connexion = sql.connect("films.db")
    cursor = connexion.execute('DELETE FROM films WHERE id = ?', (id,))
    connexion.commit()
    connexion.close()
    return {'message': 'ok delete'}