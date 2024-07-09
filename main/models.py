from django.db import models

class CountryModel(models.Model):
    name = models.CharField(max_length=100)
    capital = models.CharField(max_length=200)
    language = models.CharField(max_length=100)
    area = models.PositiveIntegerField()
    population = models.PositiveIntegerField()


    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'country'
        verbose_name_plural = 'countries'
