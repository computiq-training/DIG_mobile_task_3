from ninja import Router
from pydantic.types import UUID4
from movies.models import Serial, Season, Episode, Category
from movies.schemas import categories
from movies.schemas.episodes import EpisodesOut
from movies.schemas.general import MessageOut
from movies.schemas.seasons import SeasonOut
from movies.schemas.series import SerialOut

serial_controller = Router(tags=['Serials'])


@serial_controller.get('', response={200: list[SerialOut], 404: MessageOut})
def list_series(request):
    serial = Serial.objects.prefetch_related('categories', 'actors').all().order_by('-release_date')
    if serial:
        return 200, serial
    return 404, {'msg': 'There are no serial yet.'}


@serial_controller.get('/{id}', response={200: SerialOut, 404: MessageOut})
def get_serial_by_id(request, id: UUID4):
    try:
        serial = Serial.objects.get(id=id)
        return 200, serial
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no serial with that id.'}


@serial_controller.get('/featured', response={200: list[SerialOut], 404: MessageOut})
def featured_serial(request):
    serial = Serial.objects.filter(is_featured=True).order_by('-rating')
    if serial:
        return 200, serial
    else:
        return 404, {'msg': 'There are no featured serials.'}


# Get Seasons by Serial ID
@serial_controller.get('/{serial_id}/seasons/', response={200: list[SeasonOut], 404: MessageOut})
def list_seasons_by_id(request, serial_id: UUID4):
    seasons = Season.objects.filter(serial_id=serial_id)
    if seasons:
        return 200, seasons
    else:
        return 404, {'msg': 'There are no seasons for that serial.'}


# Get Episodes by Season ID and Serial ID
@serial_controller.get('/{serial_id}/seasons/{season_id}', response={200: list[EpisodesOut], 404: MessageOut})
def list_episodes_by_season_id_serial_id(request, serial_id: UUID4, season_id: UUID4):
    # seasons = Season.objects.get(serial_id=serial_id)
    episodes = Episode.objects.select_related('season', 'season__serial').filter(season_id=season_id)
    if episodes:
        return 200, episodes
    else:
        return 404, {'msg': 'There are no episodes for that season.'}


# /api/series/{id}/seasons/{id}/episodes/{id}`
@serial_controller.get('{serial_id}/seasons/{season_id}/episodes/{episode_id}',
                       response={200: list[EpisodesOut], 404: MessageOut})
def get_episode_by_season_id_serial_id_episode_id(request, serial_id: UUID4, season_id: UUID4, episode_id: UUID4):
    seasons = Season.objects.filter(serial_id=serial_id)

    episodes = Episode.objects.select_related('season', 'season__serial').filter(id=episode_id, season_id=season_id)
    if episodes:
        return 200, episodes
    else:
        return 404, {'msg': 'There are no episode for that season.'}
