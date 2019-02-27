import os
import json


def pied():
    table_parties = []
    for partie in os.listdir('./doliprane1000'):
        with open('./doliprane1000/' + partie, 'r') as fichier:
            stats = json.loads(fichier.read())
            print(stats)
            table_parties.append(stats)
    return table_parties


pied()
