import requests
from sqlalchemy.orm import Session

from ..config import settings
from ..schemas import Term


BASE_URL = settings.SEJM_API_BASE.rstrip('/')


def get_current_term(db: Session):
    current_term = db.query(Term).filter_by(current=True).first()
    global BASE_URL
    if current_term:
        BASE_URL = f"{BASE_URL}/term{current_term.id}"

def get_json(endpoint: str):
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    res = requests.get(url)
    res.raise_for_status()
    return res.json()
