# Generated by Django 4.0.5 on 2022-06-04 08:39

from django.db import migrations
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_category_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='children', to='store.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.category', verbose_name='Категория'),
        ),
    ]
