from django.db import models

# Create your models here.

CATEGORY_CHOICES =(
    ('CR', 'Curd'),
    ('CH', 'Cheese'),
    ('BU', 'Butter'),
    ('MI', 'Milk'),
    ('OT', 'Other'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title