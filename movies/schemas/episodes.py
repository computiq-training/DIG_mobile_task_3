from ninja import Schema
from pydantic.types import UUID4


class EpisodeOut(Schema):
    id: UUID4
    num: int