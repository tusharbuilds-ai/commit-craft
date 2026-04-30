from fastapi import APIRouter
from api.routes import home,health,craft

api_router = APIRouter()

api_router.include_router(home.router,prefix="/home")
api_router.include_router(health.router,prefix="/health")
api_router.include_router(craft.router,prefix="/craft")
