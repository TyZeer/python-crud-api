from typing import List

from fastapi import Depends, APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.products.schemas import Product, ProductCreate, ProductUpdate
from api_v1.products import crud
from core.models import db_helper
from api_v1.products.dependencies import get_product_by_id

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
    product=Depends(get_product_by_id),
):
    return product


@router.delete("/{product_id}/", response_model=Product)
async def delete_product(
    product_id: int,
    session: AsyncSession = Depends(
        db_helper.session_dependency,
    ),
):
    return await crud.delete_product_by_id(session=session, product_id=product_id)


@router.put("/{product_id}/", response_model=Product)
async def update_product(
    product_update: ProductUpdate,
    product: Product = Depends(get_product_by_id),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    return await crud.update_product(
        session=session,
        product=product,
        product_update=product_update,
    )


# @router.put("/{product_id}/", response_model=Product)
# async def update_product():
