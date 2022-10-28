from ninja import Router
from pydantic.types import UUID4

from account.authorization import TokenAuthentication
from movies.models import Serial
from movies.schemas.series import SeriesOut
from movies.schemas.general import MessageOut


from movies.models import Season
from movies.schemas.seasons import SeasonsOut

from movies.models import Episode
from movies.schemas.episodes import EpisodesOut

series_router = Router(tags=['Series'])

@series_router.get('', response={200: list[SeriesOut], 404: MessageOut})
def list_series(request):
    series = Serial.objects.all().order_by('-release_date')
    if series:
        return 200, series
    return 404, {'msg': 'There are no series yet.'}

@series_router.get('/{id}', response={200: SeriesOut, 404: MessageOut})
def get_series(request, id: UUID4):
    try:
        series = Serial.objects.get(id=id)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}

@series_router.get('/featured', response={200: list[SeriesOut], 404: MessageOut})
def featured_series(request):
    series = Serial.objects.filter(is_featured=True).order_by('-rating')
    if series:
        return 200, series
    return 404, {'msg': 'There are no featured series.'}


@series_router.get('/{id}/seasons', response={200: SeasonsOut, 404: MessageOut})
def list_seasons(request, id: UUID4):
    try:
        seasons = Season.objects.all()
        if seasons:
            return 200, seasons
        return 404, {'msg': 'There are no seasons yet.'}
    except Season.DoesNotExist:
        return 404, {'msg': 'There is no seasons with that id.'}


@series_router.get('/{id}/seasons/{season_id}', response={200: SeasonsOut, 404: MessageOut})
def get_seasons(request, season_id: UUID4):
    try:
        series = Serial.objects.get(id=season_id)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}
    
    
    
@series_router.get('/{id}/seasons/{season_id}/episodes', response={200: EpisodesOut, 404: MessageOut})
def list_episodes(request, id: UUID4):
    try:
        episodes = Episode.objects.all()
        if episodes:
            return 200, episodes
        return 404, {'msg': 'There are no episodes yet.'}
    except Episode.DoesNotExist:
        return 404, {'msg': 'There is no episodes with that id.'}


@series_router.get('/{id}/seasons/{season_id}/episodes/{episode_id}', response={200: EpisodesOut, 404: MessageOut})
def get_episodes(request, episode_id: UUID4):
    try:
        series = Episode.objects.get(id=episode_id)
        return 200, series
    except Episode.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}