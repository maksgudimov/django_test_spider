from rest_framework import generics,permissions
from .serializers import OrganizationSerializer,ProductsCompanySerializer,DistrictSerializer
from .models import Organization,Products
from fuzzywuzzy import fuzz
from django.http import HttpResponse

class OrganizationList(generics.ListAPIView):
    serializer_class = OrganizationSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        district_id = self.kwargs['district_id']
        queryset = Organization.objects.filter(district_id=district_id)
        return queryset

class ProductsList(generics.ListAPIView):
    serializer_class = ProductsCompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        organization_id = self.kwargs['organization_id']
        queryset = Products.objects.filter(organization_id=organization_id)
        return queryset

def simillitary(s1,s2):
    ready_search = fuzz.partial_ratio(s1,s2)
    return ready_search


class SearchProductsList(generics.ListAPIView):
    serializer_class = ProductsCompanySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        name_product = self.kwargs['name_product']
        mass_product_name = {}
        mass_values = []
        get_name_fuzzy = ''
        for product in Products.objects.order_by('name_product'):
            mass_product_name[product.name_product] = simillitary(name_product,product.name_product)
            mass_values.append(simillitary(name_product,product.name_product))
        values_max = max(mass_values)
        for key,value in zip(mass_product_name.keys(),mass_product_name.values()):
            if value == values_max:
                get_name_fuzzy = key
        queryset = Products.objects.filter(name_product=get_name_fuzzy)
        print(queryset)
        return queryset

class InsertProducts(generics.CreateAPIView):
    serializer_class = ProductsCompanySerializer
    queryset = Products.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save()
            return HttpResponse("OK",status=200)
        else:
            return HttpResponse("ERROR", status=400)
