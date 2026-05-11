from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=500, blank=True, null=True)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE, 
        null=True, 
        blank=True, 
        related_name='children'
    )

    def __str__(self):
        return self.name
    


class Book(models.Model):
    image = models.ImageField(upload_to="books/", blank=True, null=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    published_date = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    


    
    
