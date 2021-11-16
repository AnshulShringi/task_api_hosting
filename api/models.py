from django.db import models

# Create your models here.
class IrisDataset(models.Model):
    parameter1 = models.FloatField(blank=False, null=False)
    parameter2 = models.FloatField(blank=False, null=False)
    parameter3 = models.FloatField(blank=False, null=False)
    parameter4 = models.FloatField(blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.name