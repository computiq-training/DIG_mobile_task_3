from ninja import Schema
from pydantic.types import UUID4


class SeasonsOut(Schema):
    id: UUID4
    number: int
