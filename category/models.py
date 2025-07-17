from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'categories'

    def __str__(self):
        return self.name
