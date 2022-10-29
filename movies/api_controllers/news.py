from ninja import Router
from pydantic import UUID4

from movies.models import New
from movies.schemas.general import MessageOut
from movies.schemas.news import NewsOut

news_controller = Router(tags=['series'])


@news_controller.get('', response={200: list[NewsOut], 404: MessageOut})
def list_news(request):
    news= New.objects.all().order_by('-title')
    if news:
        return 200, news
    return 404, {'msg': 'There are no News.'}


@news_controller.get('/{id}', response={200: NewsOut, 404: MessageOut})
def get_news(request, id: UUID4):
    try:
        news = New.objects.get(id=id)
        return 200, news
    except New.DoesNotExist:
        return 404, {'msg': 'There is no news with the id yet.'}