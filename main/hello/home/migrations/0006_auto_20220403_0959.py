# Generated by Django 3.2.12 on 2022-04-03 16:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_profiles_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='id',
        ),
        migrations.AddField(
            model_name='profiles',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
