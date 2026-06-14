from .db import SessionLocal


# In api/dependencies.py (or your database helper file)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()