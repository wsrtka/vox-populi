from sqlalchemy.orm import Session

from ..utils.sejm_api import get_json
from ..schemas import Term, Party, MP


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

def ingest_parties_and_mps(db: Session):
    mps_data = get_json('/MP')
    party_cache = {}

    for mp in mps_data:
        party_name = mp['club']
        if party_name not in party_cache:
            party_obj = db.query(Party).filter_by(name=party_name).first()
            if not party_obj:
                party_obj = Party(name=party_name)
                db.add(party_obj)
                db.commit()
                db.refresh(party_obj)
            party_cache[party_name] = party_obj

        mp_obj = db.query(MP).filter_by(id=mp['id']).first()
        if not mp.obj:
            mp_obj = MP(
                id=mp['id'],
                first_name=mp['firstName'],
                last_name=mp['lastName'],
                party_id=party_cache[mp['club']].id
            )
            db.add(mp_obj)
        else:
            mp_obj.first_name = mp['firstName']
            mp_obj.last_name = mp['lastName']
            mp_obj.party_id = party_cache[mp['club']].id

    db.commit()
