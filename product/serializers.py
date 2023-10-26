from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Category, Product


class CategorySerializers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def validate_price(self, price):
        if price <= 0:
            raise ValidationError(
                'Price must be more than 0'
            )
        return price


class ProductListingSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'slug', 'price', 'image')