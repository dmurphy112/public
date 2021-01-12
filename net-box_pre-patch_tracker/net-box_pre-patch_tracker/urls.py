# first, we import the Django httpresponse library
from django.<a href="http" target="_blank">http</a> import HttpResponse
# now, we import the path module
from django.urls import path

# now let's make our function that returns our html content
def dummy_view(request):
    html = "<html><body>Pre-patch Tracker.</body></html>"
    # here we return OUR html wrapped up with the Django content
    return HttpResponse(html)

# now, we'll make our URL paths
urlpatterns = [path("", dummy_view, name = "pre-patch_list"),]

# now we have a URL path to our netbox plugin