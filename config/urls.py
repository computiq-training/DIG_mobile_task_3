from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controller import account_router
from movies.api_controllers.movies import movies_router
from movies.api_controllers.series import series_router
from movies.api_controllers.news import news_router
from movies.api_controllers.categories import categories_controller

api = NinjaAPI()
api.add_router('account/', account_router)
api.add_router('movies/', movies_router)
api.add_router('movies/', series_router)
api.add_router('movies/', news_router)
api.add_router('moives/',categories_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
