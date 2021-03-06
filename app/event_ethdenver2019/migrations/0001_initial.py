# Generated by Django 2.1.4 on 2019-01-06 18:32

from django.db import migrations, models
import django.db.models.deletion
import economy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kudos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_ETHDenver2019_Customizing_Kudos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(db_index=True, default=economy.models.get_time)),
                ('modified_on', models.DateTimeField(default=economy.models.get_time)),
                ('active', models.BooleanField(default=True)),
                ('kudos_required', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kudos.Token')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
