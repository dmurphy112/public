from django.http import HttpResponse
from . import views
from django.urls import path


def dummy_view(request):
    html = "<html><body>Animal Sounds- dummy page.</body></html>"
    return HttpResponse(html)


urlpatterns = [
    path("", dummy_view, name="animal-sounds-dummy"),
    path('random/', views.RandomAnimalView.as_view(), name = 'random_animal'),
]
