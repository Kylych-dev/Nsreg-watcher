from django.db import models


class Regcomp(models.Model):
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    note1 = models.TextField(blank=True, null=True)
    note2 = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    pricereg = models.FloatField(blank=True, null=True)
    priceprolong = models.FloatField(blank=True, null=True)
    pricechange = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'regcomp'

    def __str__(self):
        return f'{self.id}: {self.name}'

    def get_company(id):
        Regcomp.objects.get(id=id)
        