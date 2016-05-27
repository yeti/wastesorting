from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework import filters

from whatbin.api.serializers import ItemSerializer
from whatbin.models import Item

class ItemViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)