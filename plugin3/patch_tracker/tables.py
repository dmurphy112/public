'''
We need to display our pre-patches in a table format. So I will be experimenting on how to replicate
the core NetBox tabling. Currently I am following how the core tags are displayed.

Even just replication will get me 65% of the way to where I need to be.

'''

# importing our needed modules
import django_tables2 as tables
from django.conf import settings

from utilities.tables import BaseTable, BooleanColumn, ButtonsColumn, ChoiceFieldColumn, ColorColumn, ToggleColumn
from .models import ConfigContext, ObjectChange, Tag, TaggedItem

TAGGED_ITEM = """
{% if value.get_absolute_url %}
    <a href="{{ value.get_absolute_url }}">{{ value }}</a>
{% else %}
    {{ value }}
{% endif %}
"""

