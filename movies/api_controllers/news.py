from hashlib import new
from uuid import uuid4
from ninja import Router
from DIG_mobile_task_3.movies.models import New
from DIG_mobile_task_3.movies.schemas.news import NewsOut
from movies.schemas.general import MessageOut

news_controller = Router(tags=['news'])


@news_controller.get('', response={200: list[NewsOut], 404: MessageOut})
def list_news(request):
    news = New.objects.all().order_by('name')
    if news:
        return 200, news
    return 404, {'msg': "There are no news yet."}



@news_controller.get('/{id}', response={200: NewsOut, 404: MessageOut})
def get_news_id(request, id: uuid4):
    try:
        news_id = New.objects.get(id=id)
        return 200, news_id
    except New.DoesNotExist:
        return 404, {'msg': 'There is no news with that id.'}
