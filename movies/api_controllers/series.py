from ninja import Router
from pydantic.types import UUID4
from account.authorization import TokenAuthentication
from movies.schemas.general import MessageOut
from movies.schemas.series import SeriesOut
from movies.schemas.seasons import SeasonOut
from movies.schemas.episodes import EpisodenOut

from movies.models import Serial
from movies.models import Season
from movies.models import Episode




series_router = Router(tags=['Series'])

@series_router.get('', response={200: list[SeriesOut], 404: MessageOut})
def list_series(request):
    series = Serial.objects.all().order_by('-title')
    if series:
        return 200, series
    return 404, {'msg': 'There are no series yet.'}


@series_router.get('/{id}', response={200: SeriesOut, 404: MessageOut})
def get_series(request, id: UUID4):
    try:
        series =Serial.objects.get(id=id)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}


@series_router.get('/featured', response={200: list[SeriesOut], 404: MessageOut})
def featured_series(request):
    series = Serial.objects.filter(is_featured=True).order_by('-title')
    if series:
        return 200, series
    return 404, {'msg': 'There are no featured series.'}



@series_router.get('/{id}/season', response={200: list[SeasonOut],404: MessageOut})
def get_series_season(request, serial_id: UUID4):
    try:
        season=Season.objects.filter(serial_id=serial_id)
        return 200, season
    except season.DoesNotExist:
        return 404, {'msg': 'There is no season with that id series.'}





@series_router.get('/{id}/seasons/{id}/episodes', response={200: list[EpisodenOut],404: MessageOut})
def get_series_season(request, season_id:UUID4,serial_id :UUID4):
    try:
        # Hits the database.
        #e = Entry.objects.select_related('blog').get(id=5)
        #b = e.blog
        #episode=Episode.objects.select_related('season').get(season_id=season_id)
        #season=episode.objects.get(serial_id=serial_id)
        season= Season.objects.select_related('serial').filter(serial_id=serial_id)
        episode = season.objects.filter(season_id=season_id)

        return 200,episode
    except episode.DoesNotExist:
        return 404, {'msg': 'There is no episode with that id series and id season.'}

@series_router.get('/{id}/seasons/{id}/episodes/{id}', response={200: list[EpisodenOut],404: MessageOut})
def get_series_season(request, episode_id:UUID4,serial_id:UUID4,season_id):
    try:
        season = Season.objects.select_related('serial').filter(serial_id=serial_id)
        episode = season.objects.select_related('season').filter(season_id=season_id)
        episode2=episode.abjocts.filter(episode_id=episode_id)

        return 200, episode2
    except episode.DoesNotExist:
        return 404, {'msg': 'There is no episode with that id.'}