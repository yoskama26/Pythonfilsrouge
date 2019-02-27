import json

rep = []

with open("/home/robin/Bureau/fil_rouge_json/game235.json", "r") as fichier:
    readeur = fichier.read()
    if readeur:
        rep = json.loads(readeur)
    else:
        rep = []
print(rep)