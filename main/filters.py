import django_filters
from .models import Dealers, Location, County

class DealersFilter(django_filters.FilterSet):
    class Meta:
        model = Dealers
        fields = ['hardware_name',  'location', 'county']