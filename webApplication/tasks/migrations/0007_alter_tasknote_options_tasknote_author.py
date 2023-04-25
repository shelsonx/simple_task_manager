# Generated by Django 4.2 on 2023-04-22 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0006_remove_task_note_remove_tasknote_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasknote',
            options={'ordering': ('-created',)},
        ),
        migrations.AddField(
            model_name='tasknote',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]