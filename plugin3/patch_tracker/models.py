# importing needed modules to define the datatypes, like CharField, which in table land, means a string.
from django.db import models

# this will instantiate our own table, named Patches
class Patches(models.Model):
    patch = models.CharField(max_length = 50)
    tags = models.CharField(max_length = 50)

    def __str__(self):
    	return self.patch
