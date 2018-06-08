# Generated by Django 2.0.4 on 2018-06-04 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Association',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True)),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now)),
                ('mail', models.EmailField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, upload_to='associations')),
                ('site', models.URLField(blank=True)),
                ('statut', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='AssociationsManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Attend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_entry', models.DateTimeField()),
                ('ticket_number', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_begin', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('date_deadline', models.DateTimeField()),
                ('validated', models.BooleanField()),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('place', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='event')),
                ('size_intern', models.IntegerField()),
                ('size_extern', models.IntegerField()),
                ('premium', models.NullBooleanField()),
                ('token_staff', models.CharField(max_length=100)),
                ('association_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.Association')),
            ],
        ),
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(blank=True, max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name="Date d'ajout du membre")),
                ('association_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.Association')),
            ],
            options={
                'verbose_name': 'Liste des membres des associations',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='myUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_secondary', models.EmailField(blank=True, max_length=100)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Homme'), ('F', 'Femme'), ('N', 'Non binaire')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_begin', models.DateTimeField()),
                ('date_end', models.DateTimeField()),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.Event')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.myUser')),
            ],
        ),
        migrations.CreateModel(
            name='SystemAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.myUser')),
            ],
        ),
        migrations.AddField(
            model_name='members',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.myUser'),
        ),
        migrations.AddField(
            model_name='attend',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.Event'),
        ),
        migrations.AddField(
            model_name='attend',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='database.myUser'),
        ),
        migrations.AddField(
            model_name='associationsmanager',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='database.myUser'),
        ),
        migrations.AlterUniqueTogether(
            name='members',
            unique_together={('user_id', 'association_id')},
        ),
        migrations.AlterUniqueTogether(
            name='attend',
            unique_together={('user_id', 'event_id')},
        ),
    ]
