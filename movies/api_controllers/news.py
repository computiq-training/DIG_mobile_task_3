from ninja import Router
from pydantic.types import UUID4
from account.authorization import TokenAuthentication
from movies.schemas.general import MessageOut
from movies.models import New
from movies.schemas.news import NewonOut

news_router = Router(tags=['News'])

@news_router.get('', response={200: list[NewonOut], 404: MessageOut})
def list_news(request):
    news = New.objects.all().order_by('-title')
    if news:
        return 200, news
    return 404, {'msg': 'There are no New yet.'}


@news_router.get('/{id}', response={200: NewonOut, 404: MessageOut})
def get_news(request, id: UUID4):
    try:
        news =New.objects.get(id=id)
        return 200, news
    except New.DoesNotExist:
        return 404, {'msg': 'There is no New with that id.'}