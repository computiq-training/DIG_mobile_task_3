from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controller import account_router
from movies.api_controllers.movies import movies_router
from movies.api_controllers.categories import categories_controller
from movies.api_controllers.news import news_controller
from movies.api_controllers.series import series_controller

api = NinjaAPI()
api.add_router('account/', account_router)
api.add_router('movies/', movies_router)
api.add_router('Categories/', categories_controller)
api.add_router('series/', series_controller)
api.add_router('news/', news_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
