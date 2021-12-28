# Generated by Django 3.2.9 on 2021-12-28 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageprocessingapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploadModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.ImageField(upload_to='images/%Y/%m/%d')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
