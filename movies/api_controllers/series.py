from turtle import title
from ninja import Router
from pydantic.types import UUID4

from account.authorization import TokenAuthentication
from movies.models import Serial,Season,Episode
from movies.schemas.series import SeriesOut
from movies.schemas.seasons import SessonOut
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
def featured_serial(request):
    serial = Serial.objects.filter(is_featured=True).order_by('-rating')
    if serial:
        return 200, serial
    else: 
        return 404, {'msg': 'There are no featured serials.'}



@Serial_router.get('/{id}/seasons/', response={200: list[SessonOut], 404: MessageOut})
def list_seasons(request,id: UUID4):
    seasons=Season.objects.filter(id=id) 
    if seasons:
        return 200, seasons
    else: 
        return 404, {'msg': 'There are no season serials.'}



@Serial_router.get('/{id}/seasons/episodes', response={200: list[SessonOut], 404: MessageOut})
def list_seasons(request,id: UUID4):
    seasons=Season.objects.filter(id=id) 
    if seasons:
        return 200, seasons
    else: 
        return 404, {'msg': 'There are no season serials.'}



@Serial_router.get('/{id}/seasons/episodes/{id_episodes}', response={200: list[EpisodesOut], 404: MessageOut})
def list_episode(request,id: UUID4):
    episode=Episode.objects.filter(id=id) 
    if episode:
        return 200, episode
    else:  
        return 404, {'msg': 'There are no Episode  serials.'}



# @Serial_router.get('/searchable', response={200: list[SessonOut], 404: MessageOut})
# def get_serial(request, name: str):
#     movies = Serial.objects.filter(title__icontains=name)
#     if movies:
#         return 200, movies
#     return 404, {'msg': 'There is no Serial with that name.'}




