# Generated by Django 2.2.5 on 2020-06-25 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200609_0738'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login_method',
            field=models.CharField(choices=[('en', 'English'), ('kr', 'Korean')], default='email', max_length=50),
        ),
    ]
