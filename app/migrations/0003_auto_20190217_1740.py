# Generated by Django 2.1.1 on 2019-02-17 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_questions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='questions',
            name='questionData',
            field=models.FileField(upload_to=''),
        ),
    ]