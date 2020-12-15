from fastapi import APIRouter, Depends

from app.models import user_models
from app.utils import jwt_utils


router = APIRouter()


@router.get("/users/me/", response_model=user_models.User)
async def read_users_me(
    current_user: user_models.User = Depends(jwt_utils.get_current_active_user),
):
    return current_user


@router.get("/users/me/items/")
async def read_own_items(
    current_user: user_models.User = Depends(jwt_utils.get_current_active_user),
):
    return [{"item_id": "Foo", "owner": current_user.username}]
