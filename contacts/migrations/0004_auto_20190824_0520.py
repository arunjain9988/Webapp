# Generated by Django 2.2.4 on 2019-08-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20190824_0450'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='city',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='country',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='gst_no',
            field=models.CharField(default=None, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='primary_email',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='primary_phone',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='secondary_email',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='secondary_phone',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='state',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='organization',
            name='address',
            field=models.CharField(max_length=200),
        ),
    ]