from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class category(models.Model):
    category_names=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
         return self.category_names

Status_choices=[
    ('draft','Draft'),
    ('published','Published')
]
    
class articles(models.Model):
    title=models.CharField(max_length=1000)
    slug=models.SlugField(max_length=1000)
    short_description=models.TextField(max_length=10000)
    detail_description=models.TextField(max_length=100000)
    author=models.ForeignKey(to=User,on_delete=models.CASCADE)
    category=models.ForeignKey(to=category,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    image=models.ImageField(upload_to='project_final/media')
    status=models.CharField(choices=Status_choices)
    is_trending=models.BooleanField(default=False)



