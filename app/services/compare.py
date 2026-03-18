from app.services.stores import rimi_store, selver_store


def compare_basket(items: list[str]) -> dict:
    rows = []
    totals = {'Rimi': 0.0, 'Selver': 0.0, 'mixed': 0.0}

    for item in items:
        rimi = rimi_store.search(item)
        selver = selver_store.search(item)

        rimi_price = rimi['price'] if rimi else None
        selver_price = selver['price'] if selver else None

        best_store = None
        best_price = None
        if rimi_price is not None and selver_price is not None:
            if rimi_price <= selver_price:
                best_store, best_price = 'Rimi', rimi_price
            else:
                best_store, best_price = 'Selver', selver_price
        elif rimi_price is not None:
            best_store, best_price = 'Rimi', rimi_price
        elif selver_price is not None:
            best_store, best_price = 'Selver', selver_price

        if rimi_price is not None:
            totals['Rimi'] += rimi_price
        if selver_price is not None:
            totals['Selver'] += selver_price
        if best_price is not None:
            totals['mixed'] += best_price

        rows.append({
            'query': item,
            'rimi': rimi,
            'selver': selver,
            'best_store': best_store,
            'best_price': best_price,
        })

    available_totals = {k: v for k, v in totals.items() if v > 0}
    winner = min(available_totals, key=available_totals.get) if available_totals else None

    return {
        'rows': rows,
        'totals': {k: round(v, 2) for k, v in totals.items()},
        'winner': winner,
        'mode': 'demo_catalog',
        'note': 'Первая версия работает на демонстрационном каталоге. Следующий шаг — заменить demo-источники на live-поиск Rimi и Selver.',
    }
