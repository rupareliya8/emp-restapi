# Generated by Django 3.2.16 on 2022-11-21 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('loction', models.CharField(max_length=50)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non IT', 'Non IT')], max_length=50)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active_models', models.BooleanField(default=True)),
            ],
        ),
    ]
