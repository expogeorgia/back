# Generated by Django 4.2.2 on 2023-10-02 18:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('userReg', '0005_alter_user_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='user_files/')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='user_logos/')),
            ],
        ),
        migrations.CreateModel(
            name='Information_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participant', models.CharField(max_length=200)),
                ('address1', models.TextField()),
                ('address2', models.TextField(blank=True, null=True)),
                ('tel', models.TextField()),
                ('mob', models.TextField(blank=True, null=True)),
                ('mail', models.TextField(blank=True, null=True)),
                ('exhibition', models.TextField(blank=True, null=True)),
                ('contact_person', models.TextField(blank=True, null=True)),
                ('price', models.FloatField(blank=True, null=True)),
                ('payed', models.FloatField(blank=True, null=True)),
                ('status', models.BooleanField(default=False, null=True)),
                ('employer', models.TextField(blank=True, null=True)),
                ('date', models.TimeField(auto_now_add=True)),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userReg.files')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
