from django.shortcuts import render
from items.models import Item, FavoriteItem

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

from .serializers import ItemListSerializer, ItemDetailsSerializer
from .permissions import IsItemAdder

# Create your views here.
class ItemListView(ListAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemListSerializer
	filter_backends = [SearchFilter, OrderingFilter]
	search_fields = ['name']
	permission_classes = [AllowAny]


class ItemDetailView(RetrieveAPIView):
	queryset = Item.objects.all()
	serializer_class = ItemDetailsSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'item_id'
	permission_classes = [IsAuthenticated, IsItemAdder]
	# def get_queryset(self):
	# 	return Item.objects.filter(item=self.request.item, )
