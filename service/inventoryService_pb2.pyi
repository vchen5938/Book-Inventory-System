import book_pb2 as _book_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CreateBookResponse(_message.Message):
    __slots__ = ["message"]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str
    def __init__(self, message: _Optional[str] = ...) -> None: ...

class GetBookRequest(_message.Message):
    __slots__ = ["ISBN"]
    ISBN: str
    ISBN_FIELD_NUMBER: _ClassVar[int]
    def __init__(self, ISBN: _Optional[str] = ...) -> None: ...

class GetBookResponse(_message.Message):
    __slots__ = ["book", "message"]
    BOOK_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    book: _book_pb2.Book
    message: str
    def __init__(self, message: _Optional[str] = ..., book: _Optional[_Union[_book_pb2.Book, _Mapping]] = ...) -> None: ...
