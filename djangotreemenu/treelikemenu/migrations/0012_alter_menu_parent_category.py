# Generated by Django 4.2.6 on 2023-10-17 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treelikemenu', '0011_alter_menu_parent_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent_category',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='treelikemenu.category'),
        ),
    ]
