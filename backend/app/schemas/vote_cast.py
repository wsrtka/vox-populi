from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

import enum

from ..database import Base

class VoteDecision(str, enum.Enum):
    YES = "yes"
    NO = "no"
    ABSTAIN = "abstain"
    ABSENT = "absent"

class VoteCast(Base):
    __tablename__ = "votes_cast"

    id: Mapped[int] = mapped_column(primary_key=True)
    vote_id: Mapped[int] = mapped_column(ForeignKey("votes.id"))
    mp_id: Mapped[int] = mapped_column(ForeignKey("mp.id"))
    decision: Mapped[VoteDecision]

    vote = relationship("Vote", back_populates="votes_cast")
    mp = relationship("MP", back_populates="votes_cast")
