from django.shortcuts import render
from django.views.generic import ListView
from shops.models import Shop
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance

# Create your views here.


longitude = -80.191788
latitude = 25.761681

user_location = Point(longitude, latitude, srid=4326)


class ShowShop(ListView):
    template_name = "shops.html"
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location', user_location)).order_by('distance')[0:6]
