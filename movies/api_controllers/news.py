from ninja import Router
from pydantic.types import UUID4

from movies.models import New
from movies.schemas.news import NewOut
from movies.schemas.general import MessageOut

news_controller = Router(tags=['News'])


@news_controller.get('', response={200: list[NewOut], 404: MessageOut})
def list_news(request):
    news = New.objects.all().order_by('-date')
    if news:
        return 200, news
    return 404, {'msg': 'There are no News yet.'}


@news_controller.get('/{id}', response={200: list[NewOut], 404: MessageOut})
def list_news(request, id: UUID4):
    news = New.objects.filter(id=id)
    if news:
        return 200, news
    return 404, {'msg': 'There are no news with that ID.'}
