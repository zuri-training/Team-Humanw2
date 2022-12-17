# Generated by Django 4.1.4 on 2022-12-16 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccgen', '0003_alter_design_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='file',
            field=models.FileField(help_text='select the file to upload', null=True, upload_to='documents/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='download',
            name='downloaded',
            field=models.BooleanField(default=False),
        ),
    ]