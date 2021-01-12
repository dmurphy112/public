"""Administrative capabilities for patch_tracker.

Used significant amount of package config from NTC example plugin: device importe
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
from django.contrib import admin
from .models import PatchTrackerTask


@admin.register(PatchTrackerTask)
class PatchTrackerTaskAdmin(admin.ModelAdmin):
    """Administrative view for managing PatchTrackerTask instances."""

    list_display = (
        "pk",
        "created_device",
        "ip_address",
        "site",
        "role",
        "device_type",
        "platform",
        "status",
        "message",
        "failed_reason",
        "port",
        "timeout",
        "created",
    )
