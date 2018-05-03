# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import serializers, viewsets

from creamery.models import Flavor, Topping, Order


class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavor
        fields = ('name', 'url',)


class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavor.objects.all()
    serializer_class = FlavorSerializer


class ToppingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Topping
        fields = ('name', 'url',)


class ToppingViewSet(viewsets.ModelViewSet):
    queryset = Topping.objects.all()
    serializer_class = ToppingSerializer


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    order_string = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('order_string', 'topping', 'flavor')

    def get_order_string(self, obj):
        return str(obj)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
