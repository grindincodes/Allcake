# Generated by Django 3.2.5 on 2021-07-18 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeManage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CakeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cake_image', models.ImageField(blank=True, null=True, upload_to='cakeimages/')),
                ('referred_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cakeManage.store')),
            ],
        ),
    ]
