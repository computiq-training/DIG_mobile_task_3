from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controller import account_router
from movies.api_controllers.movies import movies_router

api = NinjaAPI()
api.add_router('account/', account_router)
api.add_router('movies/', movies_router)
api.add_router('serials/', serial_router)
api.add_router('news/', news_controller)
api.add_router('categories/', categories_controller)
api.add_router('actor/', actor_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
