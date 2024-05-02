from django.urls import path
from catalog.apps import NewappConfig
from catalog.views import home

app_name = NewappConfig.name
urlpatterns = [
    path('', home, name='home'),
    path('', home, name='contacts'),
]
