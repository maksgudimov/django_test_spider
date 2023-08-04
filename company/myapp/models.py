
from django.db import models


class District(models.Model):
    district = models.CharField(max_length=100)

    def __str__(self):
        return self.district

#сеть предприятий
class MonopolyCompany(models.Model):
    name_monopoly = models.CharField(max_length=100)
    description = models.TextField(default=None)
    # district_id = models.ForeignKey('District',
    #                                     on_delete=models.CASCADE)

    def __str__(self):
        return self.name_monopoly

class Organization(models.Model):
    monopoly_id = models.ForeignKey('MonopolyCompany',
                                        on_delete=models.CASCADE)
    district_id = models.ForeignKey('District',
                                        on_delete=models.CASCADE)

    name_organization = models.CharField(max_length=100)

    description = models.TextField(default=None)

    def __str__(self):
        return self.name_organization

class Products(models.Model):
    district_id = models.ForeignKey('District',
                                         on_delete=models.CASCADE)
    organization_id = models.ForeignKey('Organization',
        on_delete=models.CASCADE)
    category = models.CharField(max_length=7)
    name_product = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField(default=None)

    def __str__(self):
        return self.name_product




# Создание и сохранение объектов
# org1 = Organization(name_organization='Company Inc', description='Some description')
# org1.save()
#
# org2 = Organization(name_organization='Tech Solutions', description='Tech company')
# org2.save()
#
# company1 = Company(district='Some district', organization_id=org1, description='Company description')
# company1.save()
#
# company2 = Company(district='Another district', organization_id=org2, description='Tech company description')
# company2.save()
#
# product1 = Products(district='Some district', company_id=company1, category='Category1', name_product='Product1', price=10.99, description='Product description')
# product1.save()
#
# product2 = Products(district='Another district', company_id=company2, category='Category2', name_product='Product2', price=5.99, description='Another product description')
# product2.save()