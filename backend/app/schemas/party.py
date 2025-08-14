from sqlalchemy.orm import Mapped, mapped_column

from ..database import Base

class Party(Base):
    __tablename__ = 'parties'

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[int]
    acronym: Mapped[str]
