from django.db import models

class Qoshiqchi(models.Model):
    ism = models.CharField(max_length=255)
    t_yil = models.DateField(blank=True, null=True)
    davlat = models.CharField(max_length=50, blank=True, null=True)

class Albom(models.Model):
    nom = models.CharField(max_length=255)
    sana = models.DateField(blank=True, null=True)
    rasm = models.ImageField(upload_to='albomlar')
    qoshiqchi = models.ForeignKey(Qoshiqchi, on_delete=models.CASCADE)

class Qoshiq(models.Model):
    nom = models.CharField(max_length=255)
    janr = models.CharField(max_length=100)
    davomiylik = models.DurationField(blank=True, null=True)
    fayl = models.FileField(upload_to='qoshiqlar/', blank=True, null=True)
    albom = models.ForeignKey(Albom, on_delete=models.CASCADE)
