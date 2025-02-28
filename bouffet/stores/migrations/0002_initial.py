# Generated by Django 3.2.10 on 2023-11-08 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('stores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storeorderingsettings',
            name='changed_by',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by'),
        ),
        migrations.AddField(
            model_name='store',
            name='menu_items',
            field=models.ManyToManyField(to='stores.MenuItem'),
        ),
        migrations.AddField(
            model_name='store',
            name='opening_hours',
            field=models.ManyToManyField(to='stores.OpeningHour'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stores.menucategory'),
        ),
        migrations.AddField(
            model_name='menuitem',
            name='children_items',
            field=models.ManyToManyField(blank=True, to='stores.MenuItem'),
        ),
    ]
