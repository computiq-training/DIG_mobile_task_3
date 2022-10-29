from movies.models import New
from movies.schemas.news import Newsout
from movies.schemas.general import MessageOut
from pydantic.types import UUID4
from ninja import Router

news_controller = Router(tags=['News'])
#news
@news_controller.get('', response={200: list[Newsout], 404: MessageOut})
def list_news(request):
    news = New.objects.all().order_by('name')
    if news:
        return 200, news
    return 404, {'msg': "There are no news yet."}
    
#here we will add the news/{id}
@news_controller.get('/{id}', response={200: Newsout, 404: MessageOut})
def get_categories(request, id: UUID4):
    try:
        categories = New.objects.get(id=id)
        return 200, categories
    except New.DoesNotExist:
        return 404, {'msg': 'There is no news with that id.'}
