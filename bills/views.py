from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from products.models import Product
from clients.models import Client
from .serializers import BillSerializer
from .models import Bill
from rest_framework.permissions import IsAuthenticated


class ShowBillView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        bills = Bill.objects.filter(is_active=True)
        serializer = BillSerializer(bills, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class BillRegisterView(APIView):
    permission_classes = [IsAuthenticated]    
    def post(self, request):
        data = request.data
        
        client = Client.objects.filter(pk=data["client_id"]).first()
        if not client:
            return Response({"error": "The Client does not exist"}, status=status.HTTP_404_NOT_FOUND)

        code = Bill.objects.filter(code=data["code"]).first()
        if code:
            return Response({"error": "The Code already exist"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

        bill = Bill.objects.create(
            client_id=client,
            company_name=data["company_name"],
            nit=data["nit"],
            code=data["code"]
        )
        bill.save()

        for product in request.data['products']:
            id = product["id"]
            p = Product.objects.filter(pk=id).first()

            if not p:
                return Response({"error": f'The Product {id} does not exist'}, status=status.HTTP_404_NOT_FOUND)
            bill.products.add(p)
        
        serializer = BillSerializer(bill)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShowOneBillView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, bill_id):
        bill = Bill.objects.filter(pk=bill_id).first()
        serializer = BillSerializer(bill)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateBillView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, bill_id):
        bill = Bill.objects.get(pk=bill_id)
        if not bill:
            return Response({"error": "Bill does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        if 'company_name' in request.data:
            bill.company_name = request.data['company_name']

        if 'nit' in request.data:
            bill.nit = request.data['nit']

        if 'code' in request.data:
            code = Bill.objects.filter(code=request.data["code"]).first()
            if code:
                return Response({"error": "The Code already exist"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
            bill.code = request.data['code']

        if 'products' in request.data:
            [bill.products.remove(field.id) for field in bill.products.all()]       
            
            for product in request.data['products']:
                id = product["id"]
                p = Product.objects.filter(pk=id).first()

                if not p:
                    return Response({"error": f'The Product {id} does not exist'}, status=status.HTTP_404_NOT_FOUND)

                bill.products.add(p)

        bill.save()   
        serializer = BillSerializer(bill)

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteBillView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    def delete(self, request, bill_id):
        bill = Bill.objects.filter(pk=bill_id).first()
        if not bill:
            return Response({"error": "Bill does not exist"}, status=status.HTTP_404_NOT_FOUND)
        bill.is_active = False
        bill.save()

        return Response({"message": "Bill removed successfully"}, status=status.HTTP_200_OK)