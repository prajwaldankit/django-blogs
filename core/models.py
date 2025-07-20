from django.db import models
from post.models import Post

# Create your models here.


class Feedback(models.Model):
    name = models.CharField()
    email = models.EmailField()
    message = models.TextField()
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        db_table = 'feedbacks'
