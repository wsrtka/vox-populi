import sys
import pathlib

# Add backend to PYTHONPATH
backend_path = str(pathlib.Path(__file__).resolve().parents[1])
print(backend_path)
sys.path.append(backend_path)

from app.database import SessionLocal, Base, engine
from app.services.ingestion import ingest_terms, ingest_parties_and_mps, ingest_proceedings

# Create tables
Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()
    try:
        ingest_terms(db)
        ingest_parties_and_mps(db)
        ingest_proceedings(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()
