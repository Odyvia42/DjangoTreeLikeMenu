# Generated by Django 4.2.6 on 2023-10-17 03:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('treelikemenu', '0010_alter_menu_parent_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='parent_menu',
            field=models.ForeignKey(blank=True, default=0, null=True, on_delete=django.db.models.deletion.CASCADE, to='treelikemenu.menu'),
        ),
    ]
