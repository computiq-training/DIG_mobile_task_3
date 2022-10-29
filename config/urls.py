from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from account.controller import account_router
from movies.api_controllers.movies import movies_router
from movies.api_controllers.series import Series_controller
from movies.api_controllers.categories import categories_controller
from movies.api_controllers.news import news_controller

api = NinjaAPI()
api.add_router('account/', account_router)
api.add_router('movies/', movies_router)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
    path('categories/',categories_controller),
    path('series/', Series_controller),
    path('news/', news_controller)
]
