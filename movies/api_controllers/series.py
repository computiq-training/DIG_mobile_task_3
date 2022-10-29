from ninja import Router
from pydantic.types import UUID4

from movies.models import Serial,Season,Episode
from movies.schemas.series import SerialOut
from movies.schemas.general import MessageOut

series_router = Router(tags=['Series'])


@series_router.get('', response={200: list[SerialOut], 404: MessageOut})
def list_seiral(request):
    series = Serial.objects.all().order_by('-release_date')
    if series:
        return 200, series
    return 404, {'msg': 'There are no series yet.'}


@series_router.get('/featured', response={200: list[SerialOut], 404: MessageOut})
def featured_seiral(request):
    series = Serial.objects.filter(is_featured=True).order_by('-rating')
    if series:
        return 200, series
    return 404, {'msg': 'There are no featured series.'}


@series_router.get('/searchable', response={200: list[SerialOut], 404: MessageOut})
def get_seiral(request, name: str):
    series = Serial.objects.filter(title__icontains=name)
    if series:
        return 200, series
    return 404, {'msg': 'There is no series with that name.'}


@series_router.get('/{id}/seasons', response={200: SerialOut, 404: MessageOut})
def get_seiral(request, id: UUID4,number:int):
    try:
        series = Serial.objects.get(id=id)
        series = Season.objects.filter(number = number)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}

@series_router.get('/{id}/seasons/{id}/episodes', response={200: SerialOut, 404: MessageOut})
def get_seiral(request, id: UUID4,number:int,epi:int):
    try:
        series = Serial.objects.get(id=id)
        series = Season.objects.filter(number = number)
        series = Season.objects.get(id=id)
        series = Episode.objects.filter(number = epi)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}

@series_router.get('series/{id}/seasons/{id}/episodes/{id}', response={200: SerialOut, 404: MessageOut})
def get_seiral(request, id: UUID4,number:int,epi:int):
    try:
        series = Serial.objects.get(id=id)
        series = Season.objects.filter(number = number)
        series = Season.objects.get(id=id)
        series = Episode.objects.filter(number = epi)
        series = Episode.objects.get(id=id)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}
