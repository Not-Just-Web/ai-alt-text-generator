
from fastapi import APIRouter
from api.endpoint.alt import router as alt_text_router

router = APIRouter()
router.include_router(alt_text_router, prefix="/alt-text")