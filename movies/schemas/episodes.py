from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field

from movies.schemas.actors import ActorOut
from movies.schemas.categories import CategoryOut
from movies.schemas.seasons import SeasonOut
from movies.schemas.series import SerialOut


class EpisodesOut(Schema):
    id: UUID4
    title: str
    description: str
    trailer_url: Optional = str
    release_date: datetime.date
    rating: Decimal
    number: int
    season: SeasonOut
    length: str
   # actors: list[ActorOut]
    #categories: list[CategoryOut]
