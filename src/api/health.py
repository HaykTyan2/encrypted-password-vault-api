from fastapi import APIRouter, Depends
from src.deps import get_current_user

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/protected")
def protected_route(user: str = Depends(get_current_user)):
    return {
        "message": "Access granted",
        "user": user,
    }
