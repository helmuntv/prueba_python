from rest_framework import views, status
from rest_framework.response import Response
from .serializers import ClientSerializer, ClientMassiveUploadSerializer
from .models import Client
from bills.models import Bill
from rest_framework.permissions import IsAuthenticated
import csv, pandas as pd
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema


class ShowClientView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: ClientSerializer(many=True)})
    def get(self, request):
        clients = Client.objects.filter(is_active=True)
        serializer = ClientSerializer(clients, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ClientRegisterView(views.APIView):

    @swagger_auto_schema(request_body=ClientSerializer, responses={201: ClientSerializer()})
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShowOneClientView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(responses={200: ClientSerializer(many=True)})
    def get(self, request, client_id):
        client = Client.objects.filter(pk=client_id).first()
        serializer = ClientSerializer(client)

        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateClientView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ClientSerializer, responses={200: ClientSerializer()})
    def patch(self, request, client_id):
        client = Client.objects.filter(pk=client_id).first()
        serializer = ClientSerializer(client, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteClientView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=ClientSerializer, responses={200: ClientSerializer()})
    def delete(self, request, client_id):
        client = Client.objects.filter(pk=client_id).first()
        client.is_active = False
        client.save()

        return Response({"message": "Client removed successfully"}, status=status.HTTP_200_OK)


class ClientMassiveUploadView(views.APIView):
    serializer_class = ClientMassiveUploadSerializer

    @swagger_auto_schema()
    def post(self, request, *args, **kwarg):
        serializer = ClientMassiveUploadSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        reader = pd.read_csv(file)
        for _,row in reader.iterrows():
            serializer_client = ClientSerializer(data=dict(row))
            serializer_client.is_valid(raise_exception=True)
            serializer_client.save()
        
        return Response({"message": "Success"}, status=status.HTTP_201_CREATED)


class ClientBillsDownloadView(views.APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema()
    def get(self, request, *args, **kwargs):
        response = HttpResponse("Download success", content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="client_bills.csv"'

        writer = csv.writer(response)
        
        writer.writerow(['full_name', 'document', 'bill_quantity'])

        for client in Client.objects.all():
            bills = Bill.objects.filter(client_id=client, is_active=True)
            bills_count = bills.count()
            
            row = [client.full_name, client.document, bills_count]
            
            writer.writerow(row)

        return response