from rest_framework import serializers
from .models import Catagory,Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields=(
            "id",
            "name",
            "get_absolute_url",
            "description",
            "price",
            "get_image",
            "get_thumbnail",
            

        )
class CategorySerializer(serializers.ModelSerializer):
    products= ProductSerializer(many=True)
    class Meta:
        model= Catagory
        
        fields=(

            "id",
            "name",
            "get_absolute_url",
            "products",
        )
