# Generated by Django 4.2.3 on 2023-11-12 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_remove_lesson_created_at_assignment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quiz.lesson'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='content',
            field=models.TextField(default=None),
        ),
    ]