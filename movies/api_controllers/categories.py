from pydantic.types import UUID4
from ninja import Router

from movies.models import Category
from movies.schemas.categories import CategoryOut
from movies.schemas.general import MessageOut

categories_controller = Router(tags=['Categories'])


@categories_controller.get('', response={200: list[CategoryOut], 404: MessageOut})
def list_categories(request):
    categories = Category.objects.all().order_by('name')
    if categories:
        return 200, categories
    return 404, {'msg': "There are no categories yet."}




@categories_controller.get('/{id}', response={200: CategoryOut, 404: MessageOut})
def get_categories(request, id: UUID4):
    try:
        categories = Category.objects.get(id=id)
        return 200, categories
    except Category.DoesNotExist:
        return 404, {'msg': 'There is no categories with that id.'}
