from django.urls import path

from playground_app.views import index
from playground_app.views import page

app_name = "app"

urlpatterns = [
    path('', index, name='index'),
    path('page-<str:numero>', page, name="page"),
]
