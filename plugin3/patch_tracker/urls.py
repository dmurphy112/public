from django.http import HttpResponse

from django.urls import path
from . import views

# found app def in NetBox source, will follow convention
app_name = "patch-tracker"


def dummy_view(request):
    html = "<html><body>Patch Tracker- dummy page.</body></html>"
    return HttpResponse(html)


urlpatterns = [
    path("", dummy_view, name = "patch-tracker-dummy"),
    path("random/", views.RandomPatchView.as_view(), name='random'),
    path("<int:pk>/details", views.Details.as_view(), name="details"),
    ]

'''
Views to build:
    path("dash/", views.PatchView.as_view(), name="dash"),
    # creating temptlate URL path for pre-patch tag site, will eventually bring us to that interface page
    path("<int:pk>/front-port", views.PatchFrontPort.as_view(), name="front-port"),
'''

'''
    The angle bracket bit here tells Django to capture that data, with specified type,
    Then send it to the view function an argument. When we tell it to capture var pk, we later use this in views.py
    to pull that record from our database. That serves as the `Primary Key`
    Source: https://docs.djangoproject.com/en/3.1/intro/tutorial03/#writing-more-views
'''

