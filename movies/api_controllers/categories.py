from ninja import Router
from pydantic.types import UUID4
from movies.models import Category
from movies.schemas.categories import CategoryOut
from movies.schemas.general import MessageOut
from models import Category
categories_controller = Router(tags=['Categories'])


@categories_controller.get('', response={200: list[CategoryOut], 404: MessageOut})
def list_categories(request):
    categories = Category.objects.all().order_by('name')
    if categories:
        return 200, categories
    return 404, {'msg': "There are no categories yet."}
