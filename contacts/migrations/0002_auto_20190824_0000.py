# Generated by Django 2.2.4 on 2019-08-24 00:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='contact',
            name='address',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='contact',
            name='city',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='lname',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='mobile',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='contacts.Organization'),
            preserve_default=False,
        ),
    ]
