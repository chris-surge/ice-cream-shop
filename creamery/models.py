# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Flavor(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Topping(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Order(models.Model):
    flavor = models.ForeignKey('Flavor', on_delete=models.DO_NOTHING)
    topping = models.ForeignKey('Topping', on_delete=models.DO_NOTHING)

    def __str__(self):
        return "Someone ordered {} topped with {}".format(self.flavor, self.topping)
