from ninja import Schema
import datetime
from pydantic.types import Decimal, UUID4, Optional



class SeriesOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    thumbnail: str = None
    trailer_url: Optional = str
    release_date: datetime.date
    rating: Decimal
