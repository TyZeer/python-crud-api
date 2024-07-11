from typing import List

from fastapi import Depends, APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products.schemas import Product, ProductCreate
from api_v1.products import crud
from core.models import db_helper

router = APIRouter(tags=["Products"])


@router.get("/", response_model=List[Product])
async def get_products(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.get_products(session)


@router.post("/", response_model=Product)
async def create_product(
    product_in: ProductCreate,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
):
    return await crud.create_product(session=session, created_product=product_in)


@router.get("/{product_id}/", response_model=Product)
async def get_product(
    product_id: int,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product
    raise HTTPException(status_code=404, detail="Product not found")


@router.delete("/{product_id}/", response_model=Product)
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
):
    return await crud.delete_product(session=session, product_id=product_id)
