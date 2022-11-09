from rest_framework import serializers

from emp.models import EMPs
from product.models import Product, Category


class EMPSerializer(serializers.ModelSerializer):

    class Meta:
        model= EMPs
        fields = ('id', 'l_name', 'f_name', 'gender', 'date','numberPhone','address', 'salary','status' )


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model= Product
        fields = ('id_product', 'name', 'id_category', 'price','status' )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model= Category
        fields = ('id_category', 'name_category')

