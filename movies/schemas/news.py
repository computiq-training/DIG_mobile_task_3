from ninja import Schema
from pydantic.types import UUID4


class NewsOut(Schema):
    id: UUID4
    name: str
