from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from account.controller import account_router
from movies.api_controllers.movies import movies_router
from movies.api_controllers.series import serials_router
from movies.api_controllers.news import news_router
api = NinjaAPI()
api.add_router('account/', account_router)
api.add_router('series/', serials_router)
api.add_router('movies/', movies_router)
api.add_router('news/', news_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
