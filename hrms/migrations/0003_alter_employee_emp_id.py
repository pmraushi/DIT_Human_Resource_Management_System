# Generated by Django 3.2.7 on 2022-05-04 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0002_auto_20220504_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp250', max_length=70),
        ),
    ]
