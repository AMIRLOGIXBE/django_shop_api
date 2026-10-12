from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        def validate_price(self,price):
            if price <= 0:
                raise serializers.ValidationError("قیمت باید مثبت باشد ")
            return price
        def validate_stock(self,stock):
            if stock <= 0:
                raise serializers.ValidationError(" تعداد نباید صفر باشد ")
            return stock
