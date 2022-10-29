from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field


class SerialOut(Schema):
    id: UUID4
    title: str
    description: str
    image: str = None
    thumbnail: str = None
    trailer_url:  str = Optional 
    release_date: datetime.date
    rating: Decimal
    is_featured: bool

    

    
    
