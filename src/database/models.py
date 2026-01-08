from sqlalchemy import Column, Integer, String, LargeBinary, ForeignKey
from src.database.session import Base


class MasterCredential(Base):
    __tablename__ = "master_credentials"

    id = Column(Integer, primary_key=True)
    password_hash = Column(String, nullable=False)


class VaultEntry(Base):
    __tablename__ = "vault_entries"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    username = Column(String, nullable=False)
    encrypted_password = Column(String, nullable=False)
    salt = Column(LargeBinary, nullable=False)

