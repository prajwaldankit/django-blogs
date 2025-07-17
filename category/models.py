from django.db import models
from utils.slug import generate_unique_slug

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'categories'

    def save(self, *args, **kwargs):
        if not self.pk or Category.objects.get(pk=self.pk).name != self.name:
            self.slug = generate_unique_slug(Category, self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
