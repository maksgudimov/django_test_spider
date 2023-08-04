
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

