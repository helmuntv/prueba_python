from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated


class ShowProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductRegisterView(APIView):
    permission_classes = [IsAuthenticated]    
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShowOneProductView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProductView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteProductView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        product.is_active = False
        product.save()

        return Response({"message": "product removed successfully"}, status=status.HTTP_200_OK)