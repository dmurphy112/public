"""Plugin declaration for patch_tracker.

Used significant amount of package config from NTC example plugin: device importer
(c) 2020 Network To Code
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

__version__ = "2.1.0"

from extras.plugins import PluginConfig


class PatchTrackerConfig(PluginConfig):
    """Plugin configuration for the patch_tracker plugin."""

    name = "patch_tracker"
    verbose_name = "Patch Tracking"
    version = __version__
    author = "Daniel Murphy"
    description = "A plugin for NetBox to easily track pre-patches."
    base_url = "patch-tracker"
    required_settings = []
    min_version = "2.8.1"
    max_version = "2.10.99"
    default_settings = {}
    caching_config = {}


config = PatchTrackerConfig  # pylint:disable=invalid-name
