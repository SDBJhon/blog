# Generated by Django 3.2 on 2021-04-09 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estagio', '0006_alter_post_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('publicado', 'Publicado'), ('rascunho', 'Rascunho')], default='rascunho', max_length=10),
        ),
    ]
