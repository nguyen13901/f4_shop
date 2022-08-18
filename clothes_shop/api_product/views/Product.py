from rest_framework.viewsets import ModelViewSet

from api_product.models import Product
from api_product.serializers import ProductSerializer


class ProductView(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
