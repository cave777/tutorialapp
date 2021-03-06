# Generated by Django 2.0.5 on 2018-07-15 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0002_auto_20180709_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('status', models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('email', models.ManyToManyField(to='newsletters.NewsletterUser')),
            ],
        ),
    ]
