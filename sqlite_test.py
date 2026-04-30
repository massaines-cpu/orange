import sqlite3 as sql

connexion = sql.connect("films.db")

connexion.execute('''
            CREATE TABLE IF NOT EXISTS films (
            id INTEGER PRIMARY KEY,
            titre TEXT UNIQUE,
            annee INTEGER,
            note REAL
            )
''')
connexion.commit()
connexion.execute('INSERT OR IGNORE INTO films (titre, annee, note) VALUES (?, ?, ?)', ('Devil wears Prada', 2010, 10))
connexion.execute('INSERT OR IGNORE INTO films (titre, annee, note) VALUES (?, ?, ?)', ('Moonlight', 2019, 9.9))
connexion.execute('INSERT OR IGNORE INTO films (titre, annee, note) VALUES (?, ?, ?)', ('Hamilton', 2016, 8.5))
connexion.commit()

films = connexion.execute('SELECT * FROM films').fetchall()
print(type(films))
for film in films:
    print(film[0], film[1], film[2], film[3])