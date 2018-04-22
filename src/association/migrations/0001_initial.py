# Generated by Django 2.0.3 on 2018-04-22 16:08

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('mail', models.EmailField(max_length=100)),
                ('photo', models.ImageField(upload_to='')),
                ('site', models.URLField()),
                ('statut', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'ajout du membre")),
                ('association_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='association.Association')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='user_settings.User')),
            ],
            options={
                'verbose_name': 'Liste des membres des associations',
                'ordering': ['id'],
            },
        ),
    ]
