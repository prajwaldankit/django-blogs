from django.conf import settings
from django.db import models
from category.models import Category
from utils.slug import generate_unique_slug

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=128)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'posts'

    def save(self, *args, **kwargs):
        if not self.pk or Post.objects.get(pk=self.pk).title != self.title:
            self.slug = generate_unique_slug(Post, self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comments'

    def __str__(self):
        return f"{self.user.username} on {self.post.title}"
