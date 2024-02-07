# Generated by Django 4.2.6 on 2023-12-02 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
        ('moderators', '0001_initial'),
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ScientistInfo',
            new_name='Scientist',
        ),
        migrations.RemoveField(
            model_name='institute',
            name='structure',
        ),
        migrations.AddField(
            model_name='institute',
            name='chairman',
            field=models.CharField(default=None, max_length=200, verbose_name='Ф.И.О. председателя СМУ'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='institute',
            name='employees_count',
            field=models.IntegerField(default=1, verbose_name='Число сотрудников'),
        ),
        migrations.AddField(
            model_name='institute',
            name='scientist_count',
            field=models.IntegerField(default=0, verbose_name='Число молодых учёных'),
        ),
        migrations.AddField(
            model_name='institute',
            name='smu_link',
            field=models.URLField(blank=True, null=True, verbose_name='Ссылка на сайт СМУ института'),
        ),
    ]