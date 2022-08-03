from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def read_users(limit: int = 100, skip: int = 0):
    return {}