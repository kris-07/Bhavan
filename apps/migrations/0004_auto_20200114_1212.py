# Generated by Django 3.0.2 on 2020-01-14 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeedbackClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=100)),
                ('feedback', models.CharField(max_length=50000)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='country_code',
            field=models.CharField(default='+91', max_length=5),
        ),
    ]
