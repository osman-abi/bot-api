# Generated by Django 4.0.1 on 2022-03-16 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallMeUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=30, null=True)),
                ('page_source', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CarBuyerUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=250, null=True)),
                ('model_name', models.CharField(blank=True, max_length=250, null=True)),
                ('price_range', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=1000, null=True)),
                ('page_source', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='WaitingListUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=250, null=True)),
                ('surname', models.CharField(blank=True, max_length=250, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=250, null=True)),
                ('brand_name', models.CharField(blank=True, max_length=250, null=True)),
                ('price_range', models.CharField(blank=True, max_length=250, null=True)),
                ('page_source', models.CharField(blank=True, max_length=250, null=True)),
                ('status', models.CharField(blank=True, max_length=250, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]