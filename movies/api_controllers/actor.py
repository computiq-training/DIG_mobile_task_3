from ninja import Router

from movies.models import Actor
from movies.schemas.actors import ActorOut
from movies.schemas.general import MessageOut

actor_controller = Router(tags=['Actor'])
@actor_controller.get('', response={200: list[ActorOut], 404: MessageOut})
def list_Actor(request):
    actor = Actor.objects.all().order_by('name')
    if actor:
        return 200, actor
    return 404, {'msg': "There are no Actor yet."}