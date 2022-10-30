from turtle import title
from ninja import Router
from pydantic.types import UUID4

from account.authorization import TokenAuthentication
from movies.models import Serial,Season,Episode
from movies.schemas.series import SeriesOut
from movies.schemas.seasons import SeasonOut
from movies.schemas.episodes import EpisodesOut
from movies.schemas.general import MessageOut

Serial_router = Router(tags=['Serial'])


@Serial_router.get('', response={200: list[SeriesOut], 404: MessageOut})
def list_serial(request):
    # movies = Serial.objects.all().order_by('-release_date')
    serial = Serial.objects.all().order_by('-release_date')

    if serial:
        return 200, list(serial)
    return 404, {'msg': 'There are no Serials yet.'}


@Serial_router.get('/{id}', response={200: SeriesOut, 404: MessageOut})
def get_serial(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no Serial with that id.'}

@Serial_router.get('/featured', response={200: list[SeriesOut], 404: MessageOut})
def featured_series(request):
    series = Serial.objects.filter(is_featured=True)
    if series:
        return 200, series
    return 404, {'msg': 'There are no featured series.'}



@Serial_router.get('/{id}/season', response={200: list[SeasonOut],404: MessageOut})
def get_series_season(request, serial_id: UUID4):
    try:
        seasons=Season.objects.filter(serial_id=serial_id)
        return 200, seasons
    except Season.DoesNotExist:
        return 404, {'msg': 'There is no season with that id series.'}



@Serial_router.get('/{id}/seasons/episodes', response={200: list[EpisodesOut], 404: MessageOut})
def list_seasons(request,season_id: UUID4,):
    episode=Episode.objects.all()
    if episode:
        return 200, episode
    else:
        return 404, {'msg': 'There are no season serials.'}


@Serial_router.get('/{id}/seasons/episodes/{episodes_id}', response={200: list[EpisodesOut], 404: MessageOut})
def list_seasons(request,episode_id: UUID4,):
    episode=Episode.objects.filter(id=id)
    if episode:
        return 200, episode
    else:
        return 404, {'msg': 'There are no season serials.'}



