from movies.models import Serial
from movies.schemas.series import SerialOut
from movies.schemas.general import MessageOut
from pydantic.types import UUID4
from ninja import Router

Series_controller = Router(tags=['Series'])
#series
@Series_controller.get('', response={200: list[SerialOut], 404: MessageOut})
def list_seasons(request):
    series= Serial.objects.all().order_by('release_date')
    if series:
        return 200, series
    return 404, {'msg': "There are no seasons yet."}
    
#here we will add the SERIES/{id}
@Series_controller.get('/{id}', response={200: SerialOut, 404: MessageOut})
def get_categories(request, id: UUID4):
    try:
       series = Serial.objects.get(id=id)
       return 200, series
    except Serial.DoesNotExist:
        return 404, {'msg': 'There is no categories with that id.'}
