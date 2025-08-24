from sqlalchemy.orm import Session

from ..utils.sejm_api import get_json
from ..schemas import Term


def ingest_terms(db: Session):
    terms = get_json('/term')

    for term in terms:
        term_obj = db.query(Term).filter_by(id=term['num']).first()
        if not term_obj:
            term_obj = Term(
                id=term['num'],
                current=term['current'],
                start_date=term['from'],
                end_date=term.get('to')
            )
            db.add(term_obj)

    db.commit()

def ingest
