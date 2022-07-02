# Generated by Django 2.2 on 2022-06-27 15:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000, verbose_name='Называние')),
                ('description', models.TextField(verbose_name='Описание')),
                ('author', models.CharField(max_length=1000, verbose_name='Автор')),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='цена')),
            ],
        ),
    ]