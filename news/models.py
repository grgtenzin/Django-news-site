from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    category=models.ForeignKey(Category, on_delete=models.PROTECT)
    title=models.CharField(max_length=100, unique=True)
    slug=models.SlugField(max_length=100, unique=True)
    description=models.TextField(max_length=500)
    created_at=models.DateTimeField( auto_now_add=True)
    is_published=models.BooleanField(default=True)
    photo=models.ImageField(upload_to='photos/%Y/%M/%D')
    views=models.IntegerField(default=0)
    summary=models.TextField(max_length=250)

    def __str__(self):
        return self.title

class pages(models.Model):
    name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100)
    description=models.CharField(max_length=500)

    def __str__(self):
        return self.name
