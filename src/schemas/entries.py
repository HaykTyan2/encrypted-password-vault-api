from pydantic import BaseModel

class EntryCreate(BaseModel):
    name: str
    username: str
    secret: str
    master_password: str

class EntryOut(BaseModel):
    id: int
    name: str
    username: str

    class Config:
        from_attributes = True


class EntryReveal(BaseModel):
    master_password: str

class EntryRevealResponse(BaseModel):
    secret: str

class EntryRevealRequest(BaseModel):
    master_password: str
