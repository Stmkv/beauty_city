# Generated by Django 4.2 on 2024-12-18 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beautyservice', '0004_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата')),
                ('time', models.TimeField(verbose_name='Время')),
                ('is_active', models.BooleanField(default=True)),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='beautyservice.master')),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='beautyservice.salon')),
            ],
            options={
                'verbose_name': 'Мастер',
                'verbose_name_plural': 'Мастера',
            },
        ),
    ]
