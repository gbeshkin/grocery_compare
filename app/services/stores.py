from app.services.catalogs import RIMI_CATALOG, SELVER_CATALOG
from app.services.matcher import score


class DemoStoreAdapter:
    def __init__(self, name: str, catalog: list[dict]):
        self.name = name
        self.catalog = catalog

    def search(self, query: str) -> dict | None:
        ranked = sorted(
            self.catalog,
            key=lambda item: score(query, item),
            reverse=True,
        )
        best = ranked[0] if ranked else None
        if not best:
            return None
        best_score = score(query, best)
        if best_score < 0.45:
            return None
        return {
            'store': self.name,
            'match_score': round(best_score, 3),
            **best,
        }


rimi_store = DemoStoreAdapter('Rimi', RIMI_CATALOG)
selver_store = DemoStoreAdapter('Selver', SELVER_CATALOG)
