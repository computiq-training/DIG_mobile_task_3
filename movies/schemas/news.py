from ninja import Schema

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field



class NewsOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None