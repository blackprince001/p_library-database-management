import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from manager.database.models import Base
from manager.database.schemas.author import AuthorCreate
from manager.database.schemas.book import BookCreate


@pytest.fixture(scope="session")
def engine():
    return create_engine(url="sqlite+pysqlite:///:memory:", future=True)


@pytest.fixture(scope="session")
def author():
    return AuthorCreate(name='King Sark')


@pytest.fixture(scope="session")
def book():
    return BookCreate(title="The Lone Wolf")


@pytest.fixture
def db(engine):
    with Session(engine) as session:
        Base.metadata.create_all(bind=engine)
        yield session
