# Generated by Django 4.1.4 on 2022-12-14 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ccgen', '0002_rename_design_id_comment_design_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='design',
            name='file',
            field=models.FileField(help_text='select the file to upload', null=True, upload_to=''),
        ),
    ]