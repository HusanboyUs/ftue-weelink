# Generated by Django 4.0.3 on 2022-03-20 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_profilelink_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='topic',
            field=models.CharField(choices=[('Registration', 'Registration'), ('Profile Avatar', 'Profile Avatar'), ('Profile Settings', 'Profile Settings'), ('Another', 'Another')], max_length=22),
        ),
    ]
