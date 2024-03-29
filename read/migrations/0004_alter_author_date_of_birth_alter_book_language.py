# Generated by Django 4.2.1 on 2023-05-19 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('read', '0003_remove_book_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Y', 'YORUBA'), ('H', 'HAUSA'), ('I', 'IGBO'), ('E', 'ENGLISH')], max_length=15),
        ),
    ]
