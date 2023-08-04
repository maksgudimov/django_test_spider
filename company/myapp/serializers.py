from rest_framework import serializers
from .models import  Organization ,District,MonopolyCompany,Products

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'
        #fields = ['id','name_organization']

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class MonopolyCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MonopolyCompany
        fields = '__all__'

class ProductsCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'