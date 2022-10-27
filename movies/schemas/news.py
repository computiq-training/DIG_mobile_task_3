from ninja import Schema
import datetime
from pydantic.types import UUID4


class NewOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    date: datetime.date