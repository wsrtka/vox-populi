from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

class MP(Base):
    __tablename__ = "mp"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    party_id: Mapped[int] = mapped_column(ForeignKey("parties.id"))

    party = relationship("Party", backref="members")
