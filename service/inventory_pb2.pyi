from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
FAILURE: StatusCode
GENRE_FANTASY: Genre
GENRE_HORROR: Genre
GENRE_MYSTERY: Genre
GENRE_SCIENCE_FRICTION: Genre
GENRE_UNDEFINED: Genre
STATUS_AVAILABLE: Status
STATUS_TAKEN: Status
SUCCESS: StatusCode
UNDEFINED: StatusCode

class Book(_message.Message):
    __slots__ = ["ISBN", "author", "genre", "publishingYear", "title"]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    GENRE_FIELD_NUMBER: _ClassVar[int]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    PUBLISHINGYEAR_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    author: str
    genre: Genre
    publishingYear: int
    title: str
    def __init__(self, ISBN: _Optional[str] = ..., title: _Optional[str] = ..., author: _Optional[str] = ..., genre: _Optional[_Union[Genre, str]] = ..., publishingYear: _Optional[int] = ...) -> None: ...

class BookResponseStatus(_message.Message):
    __slots__ = ["book", "message", "statusCode"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    STATUSCODE_FIELD_NUMBER: _ClassVar[int]
    book: Book
    message: str
    statusCode: StatusCode
    def __init__(self, statusCode: _Optional[_Union[StatusCode, str]] = ..., message: _Optional[str] = ..., book: _Optional[_Union[Book, _Mapping]] = ...) -> None: ...

class ISBN(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class InventoryItem(_message.Message):
    __slots__ = ["book", "inventoryNumber", "status"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    INVENTORYNUMBER_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    book: Book
    inventoryNumber: int
    status: Status
    def __init__(self, inventoryNumber: _Optional[int] = ..., book: _Optional[_Union[Book, _Mapping]] = ..., status: _Optional[_Union[Status, str]] = ...) -> None: ...

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class StatusCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
