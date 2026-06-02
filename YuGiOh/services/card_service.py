import re

def get_image_url(card: dict) -> str | None:
    imgs = card.get("card_images") or []
    if imgs and isinstance(imgs, list):
        return imgs[0].get("image_url")
    return None


def build_query(q: str, monsters: bool, spells: bool, traps: bool, deck_card_ids: list[int] | None = None) -> dict:
    """
    Construye el filtro MongoDB combinando:
    - búsqueda por texto o por id
    - filtros por tipo (monsters/spells/traps)
    """
    q = (q or "").strip()
    filters = []

    # Filtro por deck (si viene)
    if deck_card_ids is not None:
        filters.append({"id": {"$in": deck_card_ids}})

    # Búsqueda por texto o ID
    if q:
        if q.isdigit():
            filters.append({"id": int(q)})
        else:
            safe = re.escape(q)
            filters.append({
                "$or": [
                    {"name": {"$regex": safe, "$options": "i"}},
                    {"desc": {"$regex": safe, "$options": "i"}},
                    {"race": {"$regex": safe, "$options": "i"}},
                ]
            })

    # Filtros por tipo
    type_filters = []
    if monsters:
        type_filters.append({"type": {"$regex": "Monster"}})
    if spells:
        type_filters.append({"type": "Spell Card"})
    if traps:
        type_filters.append({"type": "Trap Card"})

    if type_filters:
        filters.append({"$or": type_filters})

    if not filters:
        return {}
    if len(filters) == 1:
        return filters[0]
    return {"$and": filters}


def fetch_cards(col, q, monsters, spells, traps, limit, deck_card_ids=None):
    query = build_query(q, monsters, spells, traps, deck_card_ids=deck_card_ids)
    cards = list(col.find(query, {"_id": 0}).limit(limit))

    for c in cards:
        c["image_url"] = get_image_url(c)
        # Limpieza para que el JS no explote con las comillas
        if c.get("desc"):
            c["desc"] = c["desc"].replace("\r", "").replace("\n", " ").replace("'", "’")
    return cards