from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database.session import get_db
from src.database.models import VaultEntry
from src.schemas.entries import EntryCreate, EntryOut, EntryReveal, EntryRevealRequest
from src.services.vault import encrypt_entry, decrypt_entry
from src.deps import get_current_user
from src.schemas.entries import EntryRevealRequest, EntryRevealResponse

router = APIRouter(prefix="/entries", tags=["entries"])

@router.post("/", response_model=EntryOut)
def create_entry(
    data: EntryCreate,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    encrypted, salt = encrypt_entry(
        data.secret,
        data.master_password,
    )

    entry = VaultEntry(
        user_id=1,
        name=data.name,
        username=data.username,
        encrypted_password=encrypted,
        salt=salt,
    )

    db.add(entry)
    db.commit()
    db.refresh(entry)

    return entry

@router.get("/", response_model=list[EntryOut])
def list_entries(
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    return (
        db.query(VaultEntry)
        .filter(VaultEntry.user_id == 1)
        .all()
    )


@router.post("/{entry_id}/reveal", response_model=EntryRevealResponse)
def reveal_entry(
    entry_id: int,
    data: EntryRevealRequest,
    db: Session = Depends(get_db),
    user=Depends(get_current_user),
):
    entry = db.query(VaultEntry).filter(VaultEntry.id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    secret = decrypt_entry(
        entry.encrypted_password,
        data.master_password,
        entry.salt,
    )

    return {"secret": secret}




