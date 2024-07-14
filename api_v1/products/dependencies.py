from typing import Annotated
from fastapi import Path, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import db_helper, Product
from . import crud


async def get_product_by_id(
    product_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.session_dependency),
) -> Product:
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(status_code=404, detail="Product not found")
