# importing all the goodstuff that we need to make webpages
from django.shortcuts import render
from django.views.generic import View

# here we import the database model that we created in `models.py`
from .models import Animal

class RandomAnimalView(View):
    # this will create a random animal from our table
    def get(self, request):
        # this will pull the first animal from our database
        animal = Animal.objects.all().first()

        # this will return a rendered page. This calls on our template, `animal.html`.
        return render(request, 'netbox_animal_sounds/animal.html', {'animal':animal, })
