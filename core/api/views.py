from rest_framework.generics import ListAPIView

from core.models import Item
from .serializers import ItemSerializer


class ItemListAPIView(ListAPIView):
    model = Item
    queryset = model.objects.all()
    serializer_class = ItemSerializer
