from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base

class Proceeding(Base):
    __tablename__ = 'proceedings'

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[int]
    title: Mapped[str]

    votings = relationship("Vote", back_populates="proceedings")
