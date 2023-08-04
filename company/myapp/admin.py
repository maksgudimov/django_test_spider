from django.contrib import admin
from .models import Organization ,District,MonopolyCompany,Products



class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id','district')
    list_display_links = ('id','district')
    search_fields = ('id','district')

class MonopolyCompanyAdmin(admin.ModelAdmin):
    list_display = ('id','name_monopoly','description')
    list_display_links = ('id','name_monopoly')
    search_fields = ('id','name_organization')

class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('id','monopoly_id','district_id','name_organization','description')
    list_display_links = ('id','district_id')
    search_fields = ('id','monopoly_id','district_id','name_organization')

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id','district_id','organization_id','category','name_product','price','description')
    list_display_links = ('id','name_product')
    search_fields = ('id','category','name_product','price')


admin.site.register(District,DistrictAdmin)
admin.site.register(MonopolyCompany,MonopolyCompanyAdmin)
admin.site.register(Organization,OrganizationAdmin)
admin.site.register(Products,ProductsAdmin)
