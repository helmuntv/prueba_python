from rest_framework import views, status
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


class ShowProductView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: ProductSerializer(many=True)})
    def get(self, request):
        products = Product.objects.filter(is_active=True)
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductRegisterView(views.APIView):
    permission_classes = [IsAuthenticated]    

    @swagger_auto_schema(request_body=ProductSerializer, responses={201: ProductSerializer()})
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShowOneProductView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: ProductSerializer(many=True)})
    def get(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        serializer = ProductSerializer(product)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateProductView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ProductSerializer, responses={200: ProductSerializer()})
    def patch(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        serializer = ProductSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteProductView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema()
    def delete(self, request, product_id):
        product = Product.objects.filter(pk=product_id).first()
        product.is_active = False
        product.save()

        return Response({"message": "product removed successfully"}, status=status.HTTP_200_OK)