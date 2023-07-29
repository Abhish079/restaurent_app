# Generated by Django 4.2.1 on 2023-07-01 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Owner', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=10)),
                ('Type', models.CharField(max_length=10)),
                ('Date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
