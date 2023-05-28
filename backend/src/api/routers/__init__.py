from .users import router as users_router
from .auth import router as auth_router
from .anime import router as anime_router

routers = (users_router, auth_router, anime_router)

__all__ = ("routers",)
