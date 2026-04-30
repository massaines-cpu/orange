import sqlite3 as sql

connexion = sql.connect("films.db")

connexion.execute('''
            CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY,
            titre TEXT,
            annee INTEGER,
            note REAL
            )
''')
connexion.commit()
connexion.execute('INSERT INTO films (titre, annee, note) VALUES (?, ?, ?)', ('Devil wears Prada', 2010, 10))
connexion.execute('INSERT INTO films VALUES (?, ?, ?, ?)', ('Moonlight', 2019, 9.9))
connexion.execute('INSERT INTO TABLE films (titre, annee, note) VALUES (?, ?, ?)', ('Hamilton', 2016, 8.5))
connexion.commit()
