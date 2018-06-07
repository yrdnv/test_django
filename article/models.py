from django.db import models

# Create your models here.

class Article(models.Model):
    text = models.TextField(max_length=2048)

    def __str__(self):
        return self.text