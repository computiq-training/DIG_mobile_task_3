from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field


class EpisodesOut(Schema):
    id:UUID4
    number: int
    serial: str
  