from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from ..database import Base

class Vote(Base):
    __tablename__ = "votes"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    date: Mapped[datetime]
    title: Mapped[str]
    description: Mapped[str]
    sitting: Mapped[int]
    sitting_day: Mapped[int]
    voting_number: Mapped[int]

    votes_cast = relationship("VotesCast", back_populates="votes")
    proceedings = relationship("Proceeding", back_populates="votes")
