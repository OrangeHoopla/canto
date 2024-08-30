from rest_framework import serializers
from commerce.models import Item
from commerce.models import Category


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


# class CatSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'