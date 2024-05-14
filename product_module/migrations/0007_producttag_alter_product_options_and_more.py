# Generated by Django 4.2 on 2024-05-14 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0006_productinformation_alter_product_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=300, verbose_name='تگ محصول')),
            ],
            options={
                'verbose_name': 'تگ محصول',
                'verbose_name_plural': 'تگ های محصولات',
            },
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصول ', 'verbose_name_plural': 'محصولات  '},
        ),
        migrations.AlterModelOptions(
            name='productcategory',
            options={'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دسته بندی ها'},
        ),
        migrations.AlterModelOptions(
            name='productinformation',
            options={'verbose_name': 'اطلاعات تکمیلی محصول ', 'verbose_name_plural': 'اطلاعات تکمیلی محصولات'},
        ),
        migrations.AlterField(
            model_name='product',
            name='product_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_information', to='product_module.productinformation'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_tags',
            field=models.ManyToManyField(to='product_module.producttag'),
        ),
    ]