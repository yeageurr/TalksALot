from __future__ import annotations

from app.db_config.database_handler import Base
from datetime import datetime
from sqlalchemy import ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Messages(Base):
  __tablename__ = "messages"

  message_id: Mapped[int] = mapped_column(primary_key=True)
  message: Mapped[str] = mapped_column(Text, nullable=False)
  sender_id: Mapped[int] = mapped_column(ForeignKey("user_account.account_id", ondelete="CASCADE"), nullable=False)
  receiver_id: Mapped[int] = mapped_column(ForeignKey("user_account.account_id", ondelete="CASCADE"), nullable=False)
  sent_at: Mapped[DateTime] = mapped_column(DateTime, default=datetime.now())

  accounts = relationship(
    "Accounts",
    back_populates="messages"
  )