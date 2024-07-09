from .products.views import router as products_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(products_router, prefix="/products")
