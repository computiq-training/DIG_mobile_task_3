from ninja import Router
from pydantic.types import UUID4
from account.authorization import TokenAuthentication
from movies.models import Episode, Season, Serial
from movies.schemas.series import SerialOut
from movies.schemas.general import MessageOut

serials_router = Router(tags=['Serial'])

@serials_router.get('', response={200: list[SerialOut], 404: MessageOut})
def list_serial(request):
    serial = Serial.objects.all().order_by('-release_date')
    if serial:
        return 200, serial
    return 404, {'msg': 'There are no serial yet.'}


@serials_router.get('/featured', response={200: list[SerialOut], 404: MessageOut})
def featured_serial(request):
    serial = Serial.objects.filter(is_featured=True).order_by('-rating')
    if serial:
        return 200, serial
    return 404, {'msg': 'There are no featured serial.'}

@serials_router.get('/{id}', response={200: SerialOut, 404: MessageOut})
def get_serial(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}
    
@serials_router.get('/{id}/season', response={200: SerialOut, 404: MessageOut})
def get_serial(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        serial = Season.objects.get(id=serial)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}
    
@serials_router.get('/{id}/season/{id}/episodes', response={200: SerialOut, 404: MessageOut})
def get_serial(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        serial = Season.objects.get()
        serial = Season.objects.get(id=serial)
        serial = Episode.objects.get()
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}

@serials_router.get('/{id}/season/{id}/episodes/{id}', response={200: SerialOut, 404: MessageOut})
def get_serial(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        serial = Season.objects.get()
        serial = Season.objects.get(id=serial)
        serial = Episode.objects.get()
        serial = Episode.objects.get(id=serial)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}


