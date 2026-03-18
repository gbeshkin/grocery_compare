import re
from difflib import SequenceMatcher

SYNONYMS = {
    'молоко': 'piim',
    'milk': 'piim',
    'яйца': 'munad',
    'eggs': 'munad',
    'хлеб': 'bread',
    'бананы': 'banana',
    'банан': 'banana',
    'яблоко': 'apple',
    'яблоки': 'apple',
    'картофель': 'potato',
    'картошка': 'potato',
    'сыр': 'cheese',
    'курица': 'chicken fillet',
    'куриное филе': 'chicken fillet',
}


def normalize(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r'[^\w\s%]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return SYNONYMS.get(text, text)



def score(query: str, candidate: dict) -> float:
    q = normalize(query)
    names = [candidate['name'].lower(), *candidate.get('aliases', [])]
    best = 0.0
    for raw in names:
        c = normalize(raw)
        best = max(best, SequenceMatcher(None, q, c).ratio())
        if q in c or c in q:
            best = max(best, 0.96)
    return best
