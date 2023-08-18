from django.db import models

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=256)

    def __str__(self):
        return str(self.category_name)


class Article(models.Model):
    article_name = models.CharField(max_length=256)
    article_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    article_info = models.TextField(blank=True)
    article_data = models.DateField()
    article_image = models.ImageField(upload_to='media')

    def __str__(self):
        return str(self.article_name)





