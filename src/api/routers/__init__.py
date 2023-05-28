from .users import router as users_router
from .auth import router as auth_router

routers = (users_router, auth_router)

__all__ = ("routers",)
