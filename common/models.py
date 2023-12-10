from django.db import models


# Create your models here.


class Movie(models.Model):
    Title = models.CharField(max_length=255, verbose_name='Nomi')
    Year = models.CharField(max_length=50, verbose_name='Yili')
    Director = models.CharField(max_length=50, verbose_name='Derektori')
    Plot = models.TextField(verbose_name='Izohi')
    Country = models.CharField(max_length=13, verbose_name='Davalati')


class Galarey(models.Model):
    movie = models.ForeignKey(
        Movie,
        verbose_name='Kinosi',
        on_delete=models.CASCADE,
        related_name='Images',
    )
    image = models.ImageField(upload_to='galarey/', verbose_name='Rasmi')

    @property
    def image_url(self):
        return f'http://127.0.0.1:8000{self.image.url}'
