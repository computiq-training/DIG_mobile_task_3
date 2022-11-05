from ninja import Schema

from pydantic.types import UUID4
import datetime


class Newsout(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    release_date: datetime.data
