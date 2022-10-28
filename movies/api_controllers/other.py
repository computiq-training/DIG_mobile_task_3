from ninja import Router
from pydantic.types import UUID4
from movies.models import Actor
from movies.schemas.actors import ActorOut
from movies.schemas.general import MessageOut
