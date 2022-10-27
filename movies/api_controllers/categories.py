from uuid import uuid4
from ninja import Router
from DIG_mobile_task_3.movies.models import Category
from DIG_mobile_task_3.movies.schemas.categories import CategoryOut

from movies.models import Category
from movies.schemas.general import MessageOut

categories_controller = Router(tags=['Categories'])


@categories_controller.get('', response={200: list[CategoryOut], 404: MessageOut})
def list_categories(request):
    categories = Category.objects.all().order_by('name')
    if categories:
        return 200, categories
    return 404, {'msg': "There are no categories yet."}



@categories_controller.get('/{id}', response={200: CategoryOut, 404: MessageOut})
def get_category_id(request, id: uuid4):
    try:
        categories_id = Category.objects.get(id=id)
        return 200, categories_id
    except Category.DoesNotExist:
        return 404, {'msg': 'There is no movie with that id.'}
