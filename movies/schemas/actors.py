from ninja import Schema
import datetime
from pydantic.types import Decimal, UUID4
from pydantic import Field

class ActorOut(Schema):
    id: UUID4
    name: str
    image: str = None
