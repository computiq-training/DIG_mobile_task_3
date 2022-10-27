from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4
from pydantic import Field


class SeriesOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    thumbnail: str = None
    trailer_url: str = None
    release_date: datetime.date
    rating: Decimal
