# Generated by Django 3.1.3 on 2021-06-19 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('question_answer', '0003_activequestion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='duration',
        ),
    ]
