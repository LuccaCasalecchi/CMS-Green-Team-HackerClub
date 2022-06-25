# Generated by Django 4.0.5 on 2022-06-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsgreenteam', '0003_post_publication_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='General', max_length=50),
        ),
    ]
