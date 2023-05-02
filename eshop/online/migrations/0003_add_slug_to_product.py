# myapp/migrations/0002_add_slug_to_product.py

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('online', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=200, unique=True),
        ),
    ]