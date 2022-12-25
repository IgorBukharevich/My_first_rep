# Generated by Django 3.2.15 on 2022-12-20 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20221213_1812'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название зала')),
            ],
            options={
                'verbose_name': 'Зал',
                'verbose_name_plural': 'Залы',
            },
        ),
        migrations.AlterModelOptions(
            name='hallplace',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.RemoveField(
            model_name='registrationvisitors',
            name='place_visitor',
        ),
        migrations.AddField(
            model_name='registrationvisitors',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hall_time_show', to='mainapp.timeshow', verbose_name='Зал'),
        ),
        migrations.AddField(
            model_name='registrationvisitors',
            name='place',
            field=models.ManyToManyField(related_name='place_hall_visitor', to='mainapp.HallPlace', verbose_name='Место в зале'),
        ),
        migrations.AddField(
            model_name='hallplace',
            name='hall_name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='hall_name_place', to='mainapp.hall', verbose_name='Название зала'),
        ),
        migrations.AddField(
            model_name='timeshow',
            name='hall',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='id_hall_place', to='mainapp.hall', verbose_name='id Зала'),
        ),
    ]
