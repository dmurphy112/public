# importing PluginConfig
from extras.plugins import PluginConfig

class AnimalSoundsConfig(PluginConfig):
    name = 'netbox_animal_sounds'
    verbose_name = 'Animal Sounds'
    description = 'An example plugin for development purposes'
    version = '0.1'
    author = 'Daniel Murphy'
    author_email = 'author@example.com'
    base_url = 'animal-sounds'
    required_settings = []
    default_settings = {}
    caching_config = {}

config = AnimalSoundsConfig
