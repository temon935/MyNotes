from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Books(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Обложка', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    is_read = models.BooleanField(default=False, verbose_name='Прочитано')
    review = models.TextField(blank=True, verbose_name='Рецензия')
    rate = models.IntegerField(default=0,
                               blank=True,
                               verbose_name='Оценка',
                               validators=[MinValueValidator(0),
                                           MaxValueValidator(10)])