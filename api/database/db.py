from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.settings import conf

# Create the SQLAlchemy engine using the DATABASE_URL from settings
assert conf.DATABASE_URL is not None, "DATABASE_URL must be set!"
engine = create_engine(conf.DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session

