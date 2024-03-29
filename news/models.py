from django.db import models
from django.urls import reverse


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_ad = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    uprated_ad = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    photo = models.ImageField(upload_to='photos/%y/%m/%d/', verbose_name='Фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('view_news', kwargs={"pk": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['created_ad']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('category', kwargs={"category_id": self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']
