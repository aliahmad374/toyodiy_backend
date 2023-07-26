# Generated by Django 4.2 on 2023-07-26 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'manufacturer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'model',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('engine_code', models.TextField(blank=True, null=True)),
                ('market', models.TextField(blank=True, null=True)),
                ('part_number', models.TextField(blank=True, null=True)),
                ('part_name', models.TextField(blank=True, null=True)),
                ('quantity_required', models.IntegerField(blank=True, null=True)),
                ('part_source', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'parts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sub_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TypeYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'type_year',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='VehicleEngine',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('engine_power', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'vehicle_engine',
                'managed': False,
            },
        ),
    ]
