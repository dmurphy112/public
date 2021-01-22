# importing all the goodstuff that we need to make webpages
from django.shortcuts import render
from django.views.generic import View
# here we import the database model that we created in `models.py`
from .models import Patches

class RandomPatchView(View):
    # this will create a random animal from our table
    def get(self, request):
        # this will pull an animal from our database
        patch = Patches.objects.order_by('?').first()
        # this will return a rendered page. This calls on our template, `patch.html`.
        return render(request, 'patch_tracker/patch.html', {'patch':patch, })