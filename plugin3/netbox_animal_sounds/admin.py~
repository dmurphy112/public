# importing our admin panel module from Django, we need this for the decorator.
'''
If you don't know what a decorator is, that is fine, it is basically a special method call.
Note how we pass in our Animal database model. Just like we would with a method/function.
Just roll with it for now, don't get sucked down a documentation rabbit hole.
'''
from django.contrib import admin
# Here we import our table model that we defined in models.py
from .models import Animal

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('name', 'sound')
