dictionnaire = dict(
    {
        'prenom': "Jean",
        'nom': "Dupont",
        'age': 35
    }
)

print(dictionnaire['prenom'], dictionnaire['nom'], "a", dictionnaire['age'], "ans.")

dictionnaire['ville'] = "Paris"

print("--------------------")

new_dictionnaire = dict()
keys = ['prenom', 'ville', 'age']
values = ["Jean", "Dupont", 35]

new_dictionnaire = dict(zip(keys, values))
print(new_dictionnaire)

print("--------------------")

for i in range(len(keys)):
    new_dictionnaire[keys[i]] = values[i]
print(new_dictionnaire)

print("--------------------")

for key in new_dictionnaire:
    print("Key: ", key)

print("--------------------")

for value in new_dictionnaire.values():
    print("Value: ", value)

print("--------------------")

dictionnaire = dict(
    {
        'prenom': "Jean",
        'nom': "Dupont",
        'age': 35,
        'logement': {
            'ville': 'Paris',
            'surface': 38,
            'code_postal': "75012",
            'nb_piece': 2
        }
    }
)

print(f"La surface du logement est de", dictionnaire['logement']['surface'], "m².")