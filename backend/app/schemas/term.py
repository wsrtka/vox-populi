from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

from ..database import Base

class Term(Base):
    __tablename__ = "terms"

    id: Mapped[int] = mapped_column(primary_key=True)
    current: Mapped[bool]
    start_date: Mapped[datetime]
    end_date: Mapped[datetime]
