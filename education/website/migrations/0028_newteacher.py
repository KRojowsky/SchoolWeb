# Generated by Django 3.2.19 on 2023-09-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_alter_newstudent_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]