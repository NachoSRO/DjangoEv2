# Generated by Django 2.1.3 on 2018-11-11 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20181107_2105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mascota',
            name='folio',
        ),
        migrations.AddField(
            model_name='mascota',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mascota',
            name='vacuna',
            field=models.ManyToManyField(blank=True, to='mascota.Vacuna'),
        ),
    ]
