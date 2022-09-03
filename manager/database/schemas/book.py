from pydantic import BaseModel

from manager.database.models import Author as AuthorModel


class BookBase(BaseModel):
    title: str


class BookCreate(BookBase):
    pass


class Book(BookBase):
    title: str
    authors: list[AuthorModel] = []

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True


class BorrowedBookBase(BaseModel):
    pass


class BorrowedBookCreate(BorrowedBookBase):
    pass


class BorrowedBook(BorrowedBookBase):
    pass

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
