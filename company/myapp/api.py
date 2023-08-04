from .models import Organization ,District,MonopolyCompany,Products
from rest_framework import viewsets, permissions
from .serializers import  OrganizationSerializer,\
DistrictSerializer,MonopolyCompanySerializer,ProductsCompanySerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = OrganizationSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = DistrictSerializer

class MonopolyCompanyViewSet(viewsets.ModelViewSet):
    queryset = MonopolyCompany.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = MonopolyCompanySerializer

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = ProductsCompanySerializer


