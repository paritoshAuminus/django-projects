from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import Product, Category
from .serializer import ProductSerializer, CategorySerializer

@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_product(request, pk):
    try:
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
    except:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_categories(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
    