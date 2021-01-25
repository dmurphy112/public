# importing our admin panel module from Django, we need this for the decorator.
'''
If you don't know what a decorator is, that is fine, it is basically a special method call.
Note how we pass in our Animal database model. Just like we would with a method/function.
Just roll with it for now, don't get sucked down a documentation rabbit hole.
'''
from django.contrib import admin
# Here we import our table model that we defined in models.py
from .models import PatchTracker

@admin.register(PatchTracker)
class PatchTrackerAdmin(admin.ModelAdmin):
    '''
    To be able to modify and manage our plugin data model, we need to tell the Django Admin panel
    what to import. This will make our models accessible from the admin panel.

    We are telling the admin panel that are models are under the Patches class after importing
    that from our .models file.
    '''


    list_display = ('patch', 'site', 'tag', 'interface', 'front_port', 'rear_port')
