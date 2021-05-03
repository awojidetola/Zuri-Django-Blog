# Generated by Django 3.2 on 2021-05-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstBlog', '0003_auto_20210502_1524'),
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
            field=models.CharField(default='Data Science', max_length=255),
        ),
    ]