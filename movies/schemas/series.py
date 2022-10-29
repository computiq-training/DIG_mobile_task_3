from ninja import Schema
from pydantic.types import UUID4,Decimal
import datetime


class SerialOut(Schema):
    id: UUID4
    name: str
    release_date: datetime.data
    describtion: str
    rating: Decimal
    is_featured:bool
    thumbnail:str
    image:str
    trailer_url: str
