from fastapi import APIRouter
from .endpoints.users import user_router
from .endpoints.token import token_router

api_router = APIRouter()

api_router.include_router(user_router, prefix="/users")
api_router.include_router(token_router, prefix="/token")
