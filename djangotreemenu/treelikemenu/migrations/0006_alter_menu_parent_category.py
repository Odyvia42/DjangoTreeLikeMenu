# Generated by Django 4.2.6 on 2023-10-16 02:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treelikemenu', '0005_categody_menu_parent_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='treelikemenu.categody'),
        ),
    ]
