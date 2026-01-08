from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from src.schemas.auth import PasswordRequest, TokenResponse
from src.core.security import hash_password, verify_password, create_access_token
from src.database.session import get_db
from src.database.models import MasterCredential

router = APIRouter()

@router.post("/setup", status_code=status.HTTP_201_CREATED)
def setup_master_password(
    data: PasswordRequest,
    db: Session = Depends(get_db),
):
    existing = db.query(MasterCredential).first()
    if existing:
        raise HTTPException(
            status_code=400,
            detail="Master password already set",
        )

    credential = MasterCredential(
        password_hash=hash_password(data.password)
    )
    db.add(credential)
    db.commit()

    return {"message": "Master password initialized"}

@router.post("/login", response_model=TokenResponse)
def login(
    data: PasswordRequest,
    db: Session = Depends(get_db),
):
    credential = db.query(MasterCredential).first()
    if not credential:
        raise HTTPException(
            status_code=400,
            detail="Master password not initialized",
        )

    if not verify_password(data.password, credential.password_hash):
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials",
        )

    token = create_access_token()
    return TokenResponse(access_token=token)
