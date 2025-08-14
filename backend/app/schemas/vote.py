from sqlalchemy.orm import Mapped, mapped_column, relationship

from datetime import datetime

from ..database import Base

class Vote(Base):
    __tablename__ = "votes"

    id: Mapped[int] = mapped_column(primary_key=True)
    date: Mapped[datetime]
    title: Mapped[str]
    description: Mapped[str]

    votes_cast = relationship("VotesCast", back_populates="vote")
