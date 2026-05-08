from django.db import models

class BaseCreatedModel(models.Model):


    class Meta:
        abstract = True


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    published_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    
    
