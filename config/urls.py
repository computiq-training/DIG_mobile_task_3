from django.contrib import admin
from django.urls import path, include
from ninja import NinjaAPI

from account.controller import account_router
from movies.api_controllers.categories import categories_controller
from movies.api_controllers.movies import movies_router
from movies.api_controllers.news import news_controller
from movies.api_controllers.series import serial_controller

api = NinjaAPI()
api.add_router('account/', account_router)
api.add_router('movies/', movies_router)
api.add_router('category/', categories_controller)
api.add_router('series/', serial_controller)
api.add_router('news/', news_controller)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
