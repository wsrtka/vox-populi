from sqlalchemy.orm import Session

from ..utils.sejm_api import get_json
from ..schemas import Term, Party, MP, Proceeding, Vote


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

def ingest_proceedings(db: Session):
    proceedings = get_json('/proceedings')

    for proceeding in proceedings:
        proceeding_obj = db.query(Proceeding).filter_by(id=proceeding['id']).first()
        if not proceeding_obj:
            proceeding_obj = Proceeding(
                id=proceeding['id'],
                title=proceeding['title']
            )
            db.add(proceeding_obj)
        else:
            proceeding_obj.title = proceeding['title']
        db.commit()
        ingest_voting_for_proceeding(db, proceeding_obj.id)


def ingest_voting_for_proceeding(db: Session, proceeding_id: int):
    voting_data = get_json(f'/votings/{proceeding_id}')

    for vote in voting_data:
        # going off the assumption that voting numbers are unique per sitting, not per sitting day
        vote_obj = db.query(Vote).filter_by(sitting=vote['sitting'], voting_number=vote['votingNumber']).first()
        if not vote_obj:
            vote_obj = Vote(
                date=vote['date'],
                title=vote['title'],
                description=vote['description'],
                sitting=vote['sitting'],
                sitting_day=vote['sittingDay'],
                voting_number=vote['votingNumber']
            )
            db.add(vote_obj)
        else:
            vote_obj.date = vote['date']
            vote_obj.title = vote['title']
            vote_obj.description = vote['description']
            vote_obj.sitting = vote['sitting']
            vote_obj.sitting_day = vote['sittingDay']
            vote_obj.voting_number = vote['votingNumber']
        db.commit()
        # ingest_vote_results
