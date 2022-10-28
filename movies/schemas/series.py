from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field

from movies.models import Category
from movies.schemas.actors import ActorOut
from movies.schemas.categories import CategoryOut
from movies.schemas.news import NewsOut


class SeriesOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    thumbnail: str = None
    trailer_url: str = None
    release_date: datetime.date
    rating: Decimal
    cataogries = CategoryOut
    actors = ActorOut
