import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# твоя строка подключения
DATABASE_URL = "postgresql://postgres:9900@localhost:5432/postgres"

@pytest.fixture(scope="session")
def engine():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def db_session(engine):
    connection = engine.connect()
    transaction = connection.begin()
    Session = sessionmaker(bind=connection)
    session = Session()

    yield session

    session.close()
    transaction.rollback()
    connection.close()