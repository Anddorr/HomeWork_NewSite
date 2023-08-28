from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.category_name)


class Article(models.Model):
    article_name = models.CharField(max_length=256)
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_info = models.TextField(blank=True)
    article_data = models.DateField(default=datetime.date.today())
    article_image = models.ImageField(upload_to='media', default=None)

    def __str__(self):
        return str(self.article_name)


class Comments(models.Model):
    comment_article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_username = models.ForeignKey(User, on_delete=models.CASCADE)
    comment_data = models.DateField(default=datetime.date.today())
    comment_info = models.TextField(blank=True)






