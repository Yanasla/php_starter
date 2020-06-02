from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin
from market.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'subcategory']
        

class ProductlistView(ListModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer        
    
    def get(self,request, *args, **kwargs):
        return self.list(request, **args, **kwargs)
