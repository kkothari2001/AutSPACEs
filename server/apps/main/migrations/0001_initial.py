# Generated by Django 2.2.3 on 2019-07-15 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('openhumans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('open_humans_member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='openhumans.OpenHumansMember')),
            ],
        ),
    ]
