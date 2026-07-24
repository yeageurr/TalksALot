from __future__ import annotations

from app.db_config.database_handler import Base
from sqlalchemy import String, Text, Identity, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Accounts(Base):
  __tablename__ = "user_account"

  account_id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True)
  email: Mapped[str] = mapped_column(String(25), unique=True, nullable=False)
  username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
  hashed_password: Mapped[str] = mapped_column(Text, nullable=False)

  messages = relationship(
    "Messages",
    cascade="all, delete-orphan",
    passive_deletes=True,
    back_populates="accounts"
  )
