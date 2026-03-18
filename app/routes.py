from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.compare import compare_basket

router = APIRouter()


class CompareRequest(BaseModel):
    basket: str


@router.post('/api/compare')
async def compare(req: CompareRequest):
    basket = [line.strip() for line in req.basket.splitlines() if line.strip()]
    if not basket:
        raise HTTPException(status_code=400, detail='Корзина пустая')
    return compare_basket(basket)
