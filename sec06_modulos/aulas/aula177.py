# json.dump e json.load

# dump - converte um objeto Python em JSON e grava em um arquivo
# load - lê um arquivo JSON e converte para um objeto Python

import json
from pathlib import Path

ARQUIVO = Path(__file__).parent / "aula177.json"

filme = {
    "title": "O Senhor dos Anéis: A Sociedade do Anel",
    "original_title": "The Lord of the Rings: The Fellowship of the Ring",
    "is_movie": True,
    "imdb_rating": 8.8,
    "year": 2001,
    "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
    "budget": None,
}

with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
    json.dump(filme, arquivo, ensure_ascii=False, indent=2)

with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
    filme_do_json = json.load(arquivo)
    print(filme_do_json["title"])
