from ninja import Router
from pydantic import UUID4

from movies.models import Serial, Season, Episode
from movies.schemas.episodes import EpisodesOut
from movies.schemas.general import MessageOut
from movies.schemas.series import SeriesOut
from movies.schemas.seasons import SeasonsOut
from account.authorization import TokenAuthentication
series_controller = Router(tags=['series'])

@series_controller.get('', response={200: list[SeriesOut], 404: MessageOut})
def list_movies(request):
    series = Serial.objects.all().order_by('-title')
    if series:
        return 200, series
    return 404, {'msg': 'There are no series yet.'}
@series_controller.get('/{id}', response={200: SeriesOut, 404: MessageOut})
def get_serial_id(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}


@series_controller.get('/{featured}', response={200:  SeriesOut, 404: MessageOut})
def featured_series(request):
    series = Serial.objects.filter(is_featured=True).order_by('-title')
    if series:
        return 200, series
    return 404, {'msg': 'There are no featured series.'}
@series_controller.get('/{serial_id}/seasons/', response={200: list[SeasonsOut], 404: MessageOut})
def list_seasons(request, serial_id: UUID4):
    seasons = Season.objects.filter(serial_id=serial_id)
    if seasons:
        return 200, seasons
    else:
        return 404, {'msg': 'There are no seasons for that serial yet.'}


@series_controller.get('/{serial_id}/seasons/{season_id}', response={200: list[EpisodesOut], 404: MessageOut})
def list_episodes(request, serial_id: UUID4, season_id: UUID4):
    episodes = Episode.objects.select_related('season', 'season__serial').filter(season_id=season_id)
    if episodes:
        return 200, episodes
    else:
        return 404, {'msg': 'There are no episodes for that season yet.'}
@series_controller.get('{serial_id}/{season_id}/{episode_id}',response={200: list[EpisodesOut], 404: MessageOut})
def get_episode(request, serial_id: UUID4, season_id: UUID4, episode_id: UUID4):
    seasons = Season.objects.filter(serial_id=serial_id)
    episodes = Episode.objects.select_related('season', 'season__serial').filter(id=episode_id, season_id=season_id)
    if episodes:
        return 200, episodes
    else:
        return 404, {'msg': 'There are no episode for that season yet.'}