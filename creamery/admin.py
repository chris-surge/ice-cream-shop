# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from creamery.models import Topping, Flavor, Order

admin.site.register(Flavor)
admin.site.register(Topping)
admin.site.register(Order)