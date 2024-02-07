# Generated by Django 4.2.6 on 2024-01-31 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import documents.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('moderators', '0004_remove_queue_unique_id_type_obj_queue_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Название категории')),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название документа')),
                ('path', models.FileField(upload_to=documents.models.Doc._img_dir_path, verbose_name='Путь до документа')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='documents.category')),
                ('queue', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='moderators.queue')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]