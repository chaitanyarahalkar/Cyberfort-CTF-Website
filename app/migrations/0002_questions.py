# Generated by Django 2.1.1 on 2019-02-17 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionDescription', models.TextField()),
                ('questionPoints', models.IntegerField(default=0)),
                ('questionCategory', models.BooleanField(default=False)),
                ('questionData', models.FileField(upload_to='Uploads/')),
            ],
        ),
    ]
