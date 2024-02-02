from django.db import models
import csv
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

class Client(models.Model):
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    email = models.EmailField(max_length=255, unique=True, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField(blank=True)
    attribute_4 = models.CharField(max_length=255, blank=True) 
    def __str__(self):
        return self.name

class Bill(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='bills')
    company_name = models.CharField(max_length=255, null=False)
    nt = models.TextField(blank=True) 
    code = models.CharField(max_length=255, null=False)
    def __str__(self):
        return f"{self.company_name} - {self.client.first_name} {self.client.last_name}"

class BillProduct(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE, related_name='bill_products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='bill_products')
    def __str__(self):
        return f"{self.bill} - {self.product}"

class ClientCSVImport(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        csv_file = request.FILES.get('file')
        if not csv_file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        decoded_file = csv_file.read().decode('utf-8').splitlines()
        reader = csv.reader(decoded_file)
        clients_created = 0
        errors = []
        for row in reader:
            try:
                client, created = Client.objects.get_or_create(
                    first_name=row[0],
                    last_name=row[1],
                    email=row[2]
                )
                if created:
                    clients_created += 1
            except Exception as e:
                errors.append(str(e))
        if errors:
            return Response({"errors": errors}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": f"{clients_created} clients created successfully"}, status=status.HTTP_201_CREATED)

class ClientCSVExport(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="clients.csv"'
        writer = csv.writer(response)
        writer.writerow(['Documento', 'Nombre Completo', 'Cantidad de Facturas'])
        clients = Client.objects.annotate(bills_count=Count('bills'))
        for client in clients:
            full_name = f"{client.first_name} {client.last_name}"
            writer.writerow([client.id, full_name, client.bills_count])
        return response