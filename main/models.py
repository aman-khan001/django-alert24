from django.db import models

from tinymce.models import HTMLField

class Categories(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='category/')

    class Meta:
        verbose_name_plural = 'Category'

    def __str__(self):
        return self.title


class News(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    title = models.CharField(max_length=250)
    description = HTMLField()
    image = models.ImageField(upload_to='news/')

    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'News'
