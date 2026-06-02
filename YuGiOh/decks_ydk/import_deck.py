from pathlib import Path
from db import decks_col

def parse_ydk(path: Path) -> dict:
    """
    Devuelve un dict con:
      name: str
      main: list[int]
      extra: list[int]
      side: list[int]
      card_ids: list[int]  (main+extra+side sin duplicados, manteniendo orden)
    """
    name = path.stem  # nombre archivo sin extensión
    section = None
    main, extra, side = [], [], []

    def add_id(target_list, s):
        s = s.strip()
        if not s or s.startswith("#") or s.startswith("!"):
            return
        if s.isdigit():
            target_list.append(int(s))

    with path.open("r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()

            # Detectar sección
            if line.lower() == "#main":
                section = "main"
                continue
            if line.lower() == "#extra":
                section = "extra"
                continue
            if line.lower() == "!side":
                section = "side"
                continue

            # IDs según sección
            if section == "main":
                add_id(main, line)
            elif section == "extra":
                add_id(extra, line)
            elif section == "side":
                add_id(side, line)
            else:
                # si el fichero trae ids fuera de sección, los ignoramos
                # (o podrías meterlos en main)
                pass

    # Unir + dedupe manteniendo orden
    merged = []
    seen = set()
    for cid in main + extra + side:
        if cid not in seen:
            seen.add(cid)
            merged.append(cid)

    return {
        "name": name,
        "main": main,
        "extra": extra,
        "side": side,
        "card_ids": merged,
    }

def upsert_deck(deck: dict):
    decks_col.update_one(
        {"name": deck["name"]},
        {"$set": {
            "name": deck["name"],
            "main": deck["main"],
            "extra": deck["extra"],
            "side": deck["side"],
            "card_ids": deck["card_ids"],
        }},
        upsert=True
    )

def main():
    YDK_DIR = Path("")  # <- carpeta donde ponges tus .ydk

    if not YDK_DIR.exists() or not YDK_DIR.is_dir():
        raise SystemExit(f"No existe la carpeta: {YDK_DIR.resolve()}")

    files = sorted(YDK_DIR.glob("*.ydk"))
    if not files:
        raise SystemExit(f"No hay .ydk en: {YDK_DIR.resolve()}")

    imported = 0
    for p in files:
        deck = parse_ydk(p)
        upsert_deck(deck)
        imported += 1
        print(f"✅ {deck['name']}: main={len(deck['main'])}, extra={len(deck['extra'])}, side={len(deck['side'])}")

    print(f"\n📦 Total decks importados/actualizados: {imported}")

if __name__ == "__main__":
    main()