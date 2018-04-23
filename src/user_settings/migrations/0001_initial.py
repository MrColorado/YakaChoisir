# Generated by Django 2.0.3 on 2018-04-22 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociationsManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('mail', models.EmailField(max_length=100)),
                ('mail_secondary', models.EmailField(blank=True, max_length=100)),
                ('gender', models.CharField(choices=[('M', 'Homme'), ('F', 'Femme'), ('N', 'Non binaire')], max_length=1)),
                ('inscription_date', models.DateTimeField()),
                ('is_intern', models.BooleanField()),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'ordering': ['id'],
            },
        ),
    ]