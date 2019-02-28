import os
import json
dico2 = {}


def pied():
    table_parties = []
    for partie in os.listdir('./doliprane1000'):
        with open('./doliprane1000/' + partie, 'r') as fichier:
            stats = json.loads(fichier.read())
#            print(stats)
            table_parties.append(stats)
    return table_parties


for partie in pied():
    dateu = partie["Start time"][:8]
    if dateu in dico2:
        dico2[dateu] += 1
    else:
        dico2[dateu] = 1
print(dico2)
