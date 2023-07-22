from rest_framework import viewsets, views, permissions
from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def perform_create(self, serializer):
        serializer.save(image=self.request.data.get('image'))
    
    def get_serialiser_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        return self.serializer_class