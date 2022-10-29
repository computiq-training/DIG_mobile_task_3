from ninja import Router
from pydantic.types import UUID4

from account.authorization import TokenAuthentication
from movies.models import New
from movies.schemas.news import NewsOut
from movies.schemas.general import MessageOut

news_router = Router(tags=['News'])


@news_router.get('', response={200: list[NewsOut], 404: MessageOut})
def list_movies(request):
    news = New.objects.all().order_by('-release_date')
    if news:
        return 200, news
    return 404, {'msg': 'There are no news yet.'}



@news_router.get('/{id}', response={200: NewsOut, 404: MessageOut})
def get_news(request, id: UUID4):
    try:
        news = New.objects.get(id=id)
        return 200, news
    except New.DoesNotExist:
        return 404, {'msg': 'There is no news with that id.'}