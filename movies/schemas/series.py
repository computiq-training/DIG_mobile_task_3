from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4

from movies.schemas.actors import ActorOut
from movies.schemas.categories import CategoryOut
from movies.schemas.seasons import SeasonOut


class SerialOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    thumbnail: str = None
    trailer_url: str = None
    release_date: datetime.date
    rating: Decimal
    categories: list[CategoryOut]
    serial_actors: list[ActorOut]


class FullSerialOut(SerialOut):
    seasons: list[SeasonOut]