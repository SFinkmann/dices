# Generated by Django 3.1.8 on 2021-06-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('speechdb', '0016_auto_20210618_1344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='speechcluster',
            name='type',
        ),
        migrations.AddField(
            model_name='speech',
            name='type',
            field=models.CharField(choices=[('S', 'Soliloquy'), ('M', 'Monologue'), ('D', 'Dialogue'), ('G', 'General')], default='G', max_length=1),
            preserve_default=False,
        ),
    ]