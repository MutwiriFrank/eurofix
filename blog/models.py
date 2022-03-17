from pickletools import optimize
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):

    options = (
        ('draft', 'draft'),
        ('published', 'published')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique_for_date='publish_date')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='blog_posts', null=True)
    publish_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    status = models.CharField(max_length=20, choices=options, default='draft')

    class Meta:
        ordering = ('-publish_date',)

    def __str__(self):
        return self.title
    