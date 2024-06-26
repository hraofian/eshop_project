# Generated by Django 4.2 on 2024-06-09 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_module', '0002_alter_contactus_is_read_by_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='نام و نام خانوادگی')),
                ('photo', models.ImageField(upload_to='images')),
            ],
        ),
    ]
