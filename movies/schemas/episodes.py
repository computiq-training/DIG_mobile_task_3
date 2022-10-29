from ninja import Schema
import datetime
from pydantic.types import Decimal, UUID4, Optional


class EpisodesOut(Schema):
    id: UUID4
    number: int