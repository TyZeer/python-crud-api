from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, Result

from core.models.product import Product
from .schemas import ProductCreate, ProductUpdate, ProductPartial


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


async def delete_product(
    session: AsyncSession,
    product_id: int,
) -> Product:
    product = await get_product(session, product_id)
    if product is not None:
        await session.delete(product)
    await session.commit()
    return product


# async def update_product(  РАЗНИЦА МЕЖДУ PUT И PATCH
#     session: AsyncSession,
#     product: Product,
#     product_update: ProductUpdate,
# ) -> Product:
#     for name, value in product_update.model_dump().items():
#         setattr(product, name, value)
#     await session.commit()
#     return product
#
#
# async def update_partial(
#     session: AsyncSession,
#     product: Product,
#     product_partial: ProductPartial,
# ) -> Product:
#     for name, value in product_partial.model_dump(exclude_unset=True).items():
#         setattr(product, name, value)
#     await session.commit()
#     return product


async def update_product(
    session: AsyncSession,
    product: Product,
    updated_product: ProductUpdate | ProductPartial,
    partial: bool = False,
) -> Product | Exception:
    for key, value in updated_product.model_dump(exclude_unset=partial).items():
        setattr(product, key, value)
    await session.commit()
    return product
