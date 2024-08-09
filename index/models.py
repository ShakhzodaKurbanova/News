from django.db import models


# Create your models here.
class NewsCategory(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class News(models.Model):
    news_name = models.CharField(max_length=256)
    news_des = models.TextField(blank=True)
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.news_name

