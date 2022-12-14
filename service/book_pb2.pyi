from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor
GENRE_FANTASY: Genre
GENRE_HORROR: Genre
GENRE_MYSTERY: Genre
GENRE_SCIENCE_FRICTION: Genre
GENRE_UNDEFINED: Genre

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

class Genre(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
