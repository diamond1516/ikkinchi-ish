from django.db import models


class Player(models.Model):
    full_name = models.CharField(max_length=100, verbose_name="To'liq ismi")
    image = models.ImageField(upload_to='player/', verbose_name="Rasmi")
    created_at = models.DateField(auto_now=True)
    description = models.TextField(verbose_name='Izoh')


class Club(models.Model):
    title = models.CharField(max_length=255, verbose_name='Fudbol Klub')
    image = models.ImageField(upload_to='club/')
    created_at = models.DateField(auto_now=True)
    description = models.TextField(verbose_name='Izoh')


class Footer(models.Model):
    full_name = models.CharField(verbose_name='To\'liq ismi', max_length=50)
    image = models.ImageField(upload_to='footer/', verbose_name='Rasmi')
    description = models.TextField(verbose_name='Izoh')
