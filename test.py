
films = ["Inception", 0, "Avatar"]
films[2] = 3
print(films[0])
print(films[1])

film = ("Inception", 2010, 8.8)
print(film[0])
print(film[1])
print(film[2])

film = {"titre": "Inception", "annee": 2010, "note": 8.8}
print(film["titre"])
print(film["annee"])

films = [
    {"titre": "Inception", "annee": 2010, "note": 8.8},
    {"titre": "Titanic",   "annee": 1997, "note": 7.8},
    {"titre": "Avatar",    "annee": 2009, "note": 7.9},
]
print(films[0])
print(films[0]["titre"])