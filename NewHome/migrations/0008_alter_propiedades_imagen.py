# Generated by Django 4.1.7 on 2023-04-20 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NewHome', '0007_alter_profile_web'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propiedades',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='propiedades'),
        ),
    ]
