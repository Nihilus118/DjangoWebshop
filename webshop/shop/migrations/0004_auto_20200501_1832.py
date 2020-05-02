# Generated by Django 3.0.5 on 2020-05-01 16:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0003_auto_20200425_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestellungen',
            name='bezahlt',
        ),
        migrations.RemoveField(
            model_name='bestellungen',
            name='farbe',
        ),
        migrations.RemoveField(
            model_name='bestellungen',
            name='kasten',
        ),
        migrations.RemoveField(
            model_name='bestellungen',
            name='zahldatum',
        ),
        migrations.AddField(
            model_name='bestellungen',
            name='zahlvorgang',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Warenkorb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menge', models.IntegerField()),
                ('artikel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Artikel')),
                ('kundennummer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bestelldetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menge', models.IntegerField()),
                ('einzelpreis', models.FloatField()),
                ('artikel', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Artikel')),
                ('bestellnummer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Bestellungen')),
            ],
        ),
    ]