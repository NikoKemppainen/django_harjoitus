# Generated by Django 4.1.5 on 2023-02-06 09:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postaus',
            old_name='teskti',
            new_name='teksti',
        ),
        migrations.AddField(
            model_name='postaus',
            name='luotu',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]