from ninja import Schema
import datetime

from pydantic.types import Decimal, UUID4, Optional
from pydantic import Field


class ActorOut(Schema):
    id: UUID4
    name: str
    image: str = None
    







# "id": "79c20360-0b04-42e8-8efa-feabd24da25f",
#             "name": "Vin Diesel",
#             "image": null
#         }