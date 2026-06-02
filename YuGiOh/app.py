from flask import Flask, render_template, request
from config import DEFAULT_LIMIT
from db import cards_col, decks_col
from services.card_service import fetch_cards

app = Flask(__name__)

@app.route("/")
def index():
    limit = int(request.args.get("limit", DEFAULT_LIMIT))
    q = request.args.get("q", "")

    monsters = request.args.get("monsters") is not None
    spells = request.args.get("spells") is not None
    traps = request.args.get("traps") is not None

    # Deck seleccionado desde la URL: /?deck=K9%20Control
    selected_deck = (request.args.get("deck") or "").strip() or None

    # Lista de decks para mostrarlos en la página
    decks = list(decks_col.find({}, {"_id": 0, "name": 1}))
    decks.sort(key=lambda d: d["name"].lower())

    # Si hay deck seleccionado, obtenemos sus IDs
    deck_card_ids = None
    if selected_deck:
        deck_doc = decks_col.find_one({"name": selected_deck}, {"_id": 0, "card_ids": 1})
        deck_card_ids = (deck_doc or {}).get("card_ids", [])
        # si el deck no existe, forzamos 0 resultados
        if deck_doc is None:
            deck_card_ids = []

    # Fetch cartas (con deck opcional)
    cards = fetch_cards(
        cards_col,
        q=q,
        monsters=monsters,
        spells=spells,
        traps=traps,
        limit=limit,
        deck_card_ids=deck_card_ids
    )

    return render_template(
        "cards.html",
        cards=cards,
        decks=decks,
        selected_deck=selected_deck,
        limit=limit,
        q=q,
        monsters=monsters,
        spells=spells,
        traps=traps
    )

if __name__ == "__main__":
    app.run(debug=True)