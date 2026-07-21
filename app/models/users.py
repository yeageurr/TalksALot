from __future__ import annotations

from app.db_config.database_handler import Base
from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Accounts(Base):
  __tablename__ = "user_account"

  account_id: Mapped[int] = mapped_column(primary_key=True)
  username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
  password: Mapped[str] = mapped_column(Text, nullable=False)

  messages = relationship(
    "Messages",
    cascade="all, delete-orphan",
    passive_deletes=True,
    back_populates="accounts"
  )