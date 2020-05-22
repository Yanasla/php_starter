from rest_framework import serializers
from rest_framework import viewsets
from rest_framework import permissions

from market.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CategoryViewSet(viewsets.ModelViewSet):
    '''
    API endpoint that allow users to read and modify categories.
    '''
    queryset = Category.objects.all().order_by('id')
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]