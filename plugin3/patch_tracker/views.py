# importing all the goodstuff that we need to make webpages
from django.shortcuts import get_object_or_404, render
from django.views.generic import View
# here we import the database model that we created in `models.py`
from .models import PatchTracker

# Here we will define our testing random patch view. We will poll the database, sort, and return the first patch.
class RandomPatchView(View):
    """Display a not-so randomly selected patch"""
    def get(self, request):
        # This code responds to our get requests.

        # Now we need to create our object that contains our data.
        # using the get_object_or_404 will return a 404 code if the object doesn't exist.
        # Alternative is to throw an exception and give Dan more grays.
        patch_obj = PatchTracker.objects.order_by('?').first()

        # Now we need to return what we send to Get requests.
        # We will send a rendered version of our dashboard template.
        return render(
            request,
            'patch_tracker/random.html',
            {
                'patch':patch_obj,
            }
        )

# Here we will create our pre-patch dash tracker, this will track all FrontPorts tagged with a prepatch being monitored
class Details(View):
    # Here, we pull and filter (currently not filtering) all the entries from our model in models.py
    queryset = PatchTracker.objects.all()

    def get(self, request, pk):
        # This code responds to our get requests.

        # Now we need to create our object that contains our data.
        # using the get_object_or_404 will return a 404 code if the object doesn't exist.
        # Alternative is to throw an exception and give Dan more grays.
        patch_obj = get_object_or_404(self.queryset, pk=pk)

        # Now we need to return what we send to Get requests.
        # We will send a rendered version of our dashboard template.
        return render(
            request,
            'patch_tracker/patch_tracked.html',
            {
                'patch': patch_obj,
            }
        )