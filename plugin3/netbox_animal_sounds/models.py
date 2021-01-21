# importing needed modules to define the datatypes, like CharField, which in table land, means a string.
from django.db import models

# this will instantiate our own table, named Animals
class Animal(models.Model):
    name = models.CharField(max_length = 50)
    sound = models.CharField(max_length = 50)

    def __str__(self):
    	return self.name
