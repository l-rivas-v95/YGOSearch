import requests
import json

URL = "https://db.ygoprodeck.com/api/v7/cardinfo.php"

# Tipos considerados "antiguos"
tipos_antiguos = {
    "Normal Monster",
    "Effect Monster",
    "Fusion Monster",
    "Ritual Monster",
    "Spell Card",
    "Trap Card"
}

response = requests.get(URL)
response.raise_for_status()

data = response.json()["data"]

cartas_antiguas = []

for carta in data:
    if carta["type"] in tipos_antiguos:
        cartas_antiguas.append(carta)

cartas_antiguas = []

for carta in data:
    if carta["type"] in tipos_antiguos:
        cartas_antiguas.append(carta)

# GUARDAMOS SOLO LA LISTA
with open("yugioh_cartas_antiguas_mongodb.json", "w", encoding="utf-8") as f:
    json.dump(cartas_antiguas, f, indent=4, ensure_ascii=False)

print("✅ JSON preparado para MongoDB")
print("📊 Total cartas antiguas:", len(cartas_antiguas))