from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field

from movies.schemas.actors import ActorOut
from movies.schemas.categories import CategoryOut


class SerialOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    release_date: datetime.date
    rating: Decimal
    categories: list[CategoryOut]
    actors: list[ActorOut]
