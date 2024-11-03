"""Description.

Script pour scraper la liste des entreprises du
SP500 via wikipedia.
"""

from requests import get
from bs4 import BeautifulSoup
from dataclasses import dataclass
import json

ADRESSE = "https://www.tennisendirect.net/atp/classement/"

reponse = get(ADRESSE)
assert reponse.status_code == 200


entreprises = [genere_ligne(ligne) for ligne in lignes]

with open("entreprises.json", "w") as fichier:
    fichier.write(json.dumps([entreprise.__dict__ for entreprise in entreprises]))