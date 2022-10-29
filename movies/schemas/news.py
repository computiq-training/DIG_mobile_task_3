from ninja import Schema
import datetime
from pydantic.types import Decimal, UUID4, Optional


class NewsOut(Schema):
    id: UUID4
    title: str
    description: str
    date: datetime.date
    image: str= None