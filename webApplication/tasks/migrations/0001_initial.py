# Generated by Django 4.2 on 2023-04-21 02:12

from django.db import migrations, models
import django.db.models.deletion
import tasks.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskPriority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name=tasks.models.TaskPriority)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('priority', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.taskpriority')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tasks.tasktype')),
            ],
        ),
    ]
