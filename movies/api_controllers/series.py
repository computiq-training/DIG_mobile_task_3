from ninja import Router
from pydantic.types import UUID4

from movies.models import Serial
from movies.schemas.general import MessageOut
from movies.schemas.series import SeriesOut

series_router = Router(tags=['Series'])



@series_router.get('', response= {200 : list[SeriesOut], 404 : MessageOut})
def list_series(request):
    series = Serial.objects.all().order_by('release_date')
    if series:
        return 200 ,series
    return 404 ,  {'msg': 'There are no series yet.'}

@series_router.get('/searchable', response={200: list[SeriesOut], 404: MessageOut})
def get_series(request, name: str):
    series = Serial.objects.filter(title__icontains=name)
    if series:
        return 200, series
    return 404, {'msg': 'There is no series with that name.'}


@series_router.get('/{id}', response={200: SeriesOut, 404: MessageOut})
def get_series(request, id: UUID4):
    try:
        series = Serial.objects.get(id=id)
        return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no series with that id.'}