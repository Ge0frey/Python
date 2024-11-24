from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    
    class Meta:
        verbose_name_plural = 'cities'
    
    def __str__(self):
        return f"{self.name}, {self.country_code}" 