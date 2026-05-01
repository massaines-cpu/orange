import pandas as pd

films = [
    {'titre': 'Parasite',                              'annee': 2019, 'note': 8.6},
    {'titre': 'Hereditary',                            'annee': 2018, 'note': 7.3},
    {'titre': 'Midsommar',                             'annee': 2019, 'note': 7.1},
    {'titre': 'Portrait de la jeune fille en feu',     'annee': 2019, 'note': 8.1},
]

df = pd.DataFrame(films)
df.to_csv('films.csv', index=False)