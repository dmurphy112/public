# importing needed modules to define the datatypes, like CharField, which in table land, means a string.
from django.db import models
from extras.models import ChangeLoggedModel
# this is a pre-defined class that netbox uses and we pass into our model

# adding in code to support permissions later down the road
from utilities.querysets import RestrictedQuerySet
class BgpPeering(ChangeLoggedModel):
  objects = RestrictedQuerySet.as_manager()


# this will instantiate our own table, named Patches
class PatchTracker(ChangeLoggedModel):
    '''
    Here we define the Django data models that we will be using with our plugin.
    This is an excerpt from my notes in Roam on how to structure the model refs.
    When calling to an existing model, we use the `ForeignKey` call, and specify what model we are linking to.
    We link to the model with the `to=` arg.
    `on_delete=models.SET_NULL` tells Django (and our underlying SQL engine) what to do when the model we link to gets
        deleted. This flag will set the value of our entry to NULL. This requires the `null=True` arg below.
        This is the same behavior as the SQL Constraint. It is not implemented in SQL, this is Django behavior.
    `blank=True` tells Django that when entering the data into forms, this filed IS NOT mandatory.
    `null=True`  Tells Django and that we are allowed to have a null value in this model's table column. Needed for above.

    We will be using pre-defined database models with the exception of the `Patch` model. This is reserved for future
    use and is expected to be used when assigning patches from the plugin.
    For the site and tag models, we will be linking to the existing NetBox model. This is mandatory.
    Models: patch, site, tag, cable_termination, path_endpoint, interface, front_port, rear_port
    '''

    patch = models.CharField(max_length = 50)
    # linking to the existing NetBox Site model, we have to call it from where it's defined in the DCIM app.
    site = models.ForeignKey(to="dcim.Site",on_delete=models.SET_NULL, blank=True, null=True)
    # linking to the existing NetBox Tag model, we have to call it from where it's defined in the Extras app.
    tag = models.ForeignKey(to="extras.Tag", on_delete=models.SET_NULL, blank=True, null=True)
    # linking to the existing NetBox Site model, we have to call it from where it's defined in the DCIM app.
    '''
    commenting out the below after getting errors on the Django Migration that:
    TypeError: Cannot create a consistent method resolution order (MRO) for bases Model, ChangeLoggedModel
    '''
    # cable_termination = models.ForeignKey(to="dcim.CableTermination", on_delete=models.SET_NULL, blank=True, null=True)
    # path_endpoint = models.ForeignKey(to="extras.PathEndpoint", on_delete=models.SET_NULL, blank=True, null=True)
    interface = models.ForeignKey(to="dcim.Interface", on_delete=models.SET_NULL, blank=True, null=True)

    front_port = models.ForeignKey(to="dcim.FrontPort", on_delete=models.SET_NULL, blank=True, null=True)
    rear_port = models.ForeignKey(to="dcim.RearPort", on_delete=models.SET_NULL, blank=True, null=True)

    # this below will return the instance name of our model. Not so sure we need it, will comment out for now.
    # this block is from the NetBox documentation, not the blog post.

    def __str__(self):
        return self.patch



