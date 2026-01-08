from pydantic import BaseModel, Field

class PasswordRequest(BaseModel):
    password: str = Field(min_length=12)

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
