# Generated by Django 2.2 on 2019-05-02 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('babybuddy', '0005_auto_20190502_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('sv', 'Swedish')], default='en', max_length=255, verbose_name='Language'),
        ),
    ]