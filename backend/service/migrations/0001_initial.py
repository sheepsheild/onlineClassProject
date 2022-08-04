# Generated by Django 4.0.3 on 2022-04-21 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_number_limit', models.BigIntegerField()),
                ('organizing_time_limit', models.BigIntegerField()),
                ('period', models.CharField(choices=[('OMO', 'یک ماهه'), ('TMO', 'سه ماهه'), ('SMO', 'شش ماهه'), ('OYR', 'یک ساله')], max_length=3)),
                ('price', models.BigIntegerField()),
                ('discount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.plan')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
