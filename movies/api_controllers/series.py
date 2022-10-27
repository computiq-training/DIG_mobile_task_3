from typing import List
from ninja import Router
from pydantic.types import UUID4
from movies.models import Serial
from movies.models import Season
from movies.models import Episode
from movies.schemas.series import SeriesOut
from movies.schemas.seasons import SeasonsOut
from movies.schemas.episodes import EpisodesOut
from movies.schemas.general import MessageOut

series_router = Router(tags=['series'])

 # Method Get List of Series

@series_router.get('', response={200: list[SeriesOut], 404: MessageOut})
def list_series(request):
    series = Serial.objects.all().order_by('-release_date')
    if series:
        return 200, series
    return 404, {'msg': 'There are no series yet.'}


 # Method Get Serial by id

@series_router.get('/{id}', response={200: SeriesOut, 404: MessageOut})
def get_serial_id(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}



 # Method Get Featured Series

@series_router.get('/featured', response={200: list[SeriesOut], 404: MessageOut})
def featured_series(request):
    series = Serial.objects.filter(is_featured=True).order_by('-rating')
    if series:
        return 200, series
    return 404, {'msg': 'There are no featured series.'}


 # Method Get Seasons by Id of Serial
 
@series_router.get('/{id}/seasons', response={200: List[SeasonsOut], 404: MessageOut})
def get_seasons(request, id: UUID4):
    try:
        season = Season.objects.get(id=id)
        return 200, season
    except Season.DoesNotExist:
        return 404, {'msg': 'There is no seasons serial with that id.'}


 # Method Get episodes by Id of Serial and Id of Seasons

@series_router.get('/{id}/seasons/{id}/episodes', response={200: List[EpisodesOut], 404: MessageOut})
def get_episodes(request, id: UUID4):
    try:
        episodes = Episode.objects.get(id=id)
        return 200, episodes
    except Episode.DoesNotExist:
        return 404, {'msg': 'There is no episodes serial with that seasons id.'}


# Method Get episodes by Id of Serial and Id of Seasons

@series_router.get('/{id}/seasons/{id}/episodes/{id}', response={200: EpisodesOut, 404: MessageOut})
def get_episodes_id(request, id: UUID4):
    try:
        episodes_id = Episode.objects.get(id=id)
        return 200, episodes_id
    except Episode.DoesNotExist:
        return 404, {'msg': 'There is no episodes serial with that id.'}

 # Method Search Name of Series

@series_router.get('/searchable', response={200: list[SeriesOut], 404: MessageOut})
def get_movie(request, name: str):
    series = Serial.objects.filter(title__icontains=name)
    if series:
        return 200, series
    return 404, {'msg': 'There is no serial with that name.'}
 
