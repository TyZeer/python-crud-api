from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from core.models.product import Product
from .schemas import ProductCreate


async def get_products(session: AsyncSession) -> list[Product]:
    stmt = select(Product).order_by(Product.id)
    result: Result = await session.execute(stmt)
    products = result.scalars().all()
    return list(products)


async def get_product(session: AsyncSession, product_id: int) -> Product | None:
    return await session.get(Product, product_id)
    # stmt = select(Product).where(Product.id == product_id)


async def create_product(
    session: AsyncSession, created_product: ProductCreate
) -> Product | Exception:
    product = Product(**created_product.model_dump())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product
