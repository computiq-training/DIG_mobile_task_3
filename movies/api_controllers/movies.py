from ninja import Router
from pydantic.types import UUID4

from account.authorization import TokenAuthentication
from movies.models import Movie
from movies.schemas.movies import MovieOut
from movies.schemas.general import MessageOut

movies_router = Router(tags=['Movies'])


@movies_router.get('', response={200: list[MovieOut], 404: MessageOut})
def list_movies(request):
    movies = Movie.objects.all().order_by('-release_date')
    if movies:
        return 200, movies
    return 404, {'msg': 'There are no movies yet.'}


@movies_router.get('/featured', response={200: list[MovieOut], 404: MessageOut})
def featured_movies(request):
    movies = Movie.objects.filter(is_featured=True).order_by('-rating')
    if movies:
        return 200, movies
    return 404, {'msg': 'There are no featured movies.'}


@movies_router.get('/favorites', auth=TokenAuthentication(), response={200: list[MovieOut], 404: MessageOut})
def favorite_movies(request):
    pass


@movies_router.get('/searchable', response={200: list[MovieOut], 404: MessageOut})
def get_movie(request, name: str):
    movies = Movie.objects.filter(title__icontains=name)
    if movies:
        return 200, movies
    return 404, {'msg': 'There is no movie with that name.'}


@movies_router.get('/{id}', response={200: MovieOut, 404: MessageOut})
def get_movie(request, id: UUID4):
    try:
        movie = Movie.objects.get(id=id)
        return 200, movie
    except Movie.DoesNotExist:
        return 404, {'msg': 'There is no movie with that id.'}
