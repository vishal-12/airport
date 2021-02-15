# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Lounge.models import AirpotLoungeModel
from Lounge.forms import LoungeProjectsFrom

admin.site.register(AirpotLoungeModel)

# class MochaProjectsAdmin(admin.ModelAdmin):
#     form = LoungeProjectsFrom
#
#
# admin.site.register(AirpotLoungeModel)