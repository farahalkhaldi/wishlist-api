from rest_framework import serializers
from django.contrib.auth.models import User
from items.models import Item, FavoriteItem

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['first_name' , 'last_name']

class ItemListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name = "itemapi-detail",
		lookup_field = "id",
		lookup_url_kwarg = "item_id"
		)

	added_by = UserSerializer()
	favorited_by = serializers.SerializerMethodField()

	class Meta:
		model = Item
		fields = ['id', 'name', 'image', 'description', 'added_by', 'detail', "favorited_by"]

	def get_favorited_by(self, obj):
		return FavoriteItem.objects.filter(item=obj).count()

class FavoriteItemSerializer(serializers.ModelSerializer):
	class Meta:
		model = FavoriteItem
		fields = ['user']

class ItemDetailsSerializer(serializers.ModelSerializer):
	added_by = UserSerializer()
	favorited_by = serializers.SerializerMethodField()


	class Meta:
		model = Item
		fields = '__all__'


	def get_favorited_by(self, obj):
		favs = FavoriteItem.objects.filter(item=obj)
		serializer = FavoriteItemSerializer(favs, many=True)
		return serializer.data