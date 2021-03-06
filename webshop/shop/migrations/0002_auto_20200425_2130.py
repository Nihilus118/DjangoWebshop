# Generated by Django 3.0.5 on 2020-04-25 19:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farben',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('verfuegbar', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Kaesten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beschreibung', models.CharField(max_length=150)),
                ('groesse', models.CharField(max_length=50)),
                ('verfuegbar', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bestellungen',
            fields=[
                ('bestellnummer', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('bestelldatum', models.DateTimeField(auto_now_add=True)),
                ('stadt', models.CharField(max_length=30)),
                ('strasse', models.CharField(max_length=50)),
                ('hausnummer', models.CharField(max_length=5)),
                ('bezahlt', models.BooleanField(default=True)),
                ('zahldatum', models.DateTimeField()),
                ('farbe', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Farben')),
                ('kasten', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Kaesten')),
                ('kundennummer', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='artikel',
            name='farbe_kasten',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Farben'),
        ),
        migrations.AddField(
            model_name='artikel',
            name='groesse_kasten',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='shop.Kaesten'),
        ),
    ]
