# Generated by Django 3.1.6 on 2021-02-12 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_auto_20210212_1224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='allergens',
            options={'verbose_name_plural': 'Allergens'},
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='allergens',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='menu.allergens'),
        ),
    ]